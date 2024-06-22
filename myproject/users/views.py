from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib import messages
from .models import CustomUser
import random


def login_and_register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                django_login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL after successful login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='/users/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required(login_url='/users/login/')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('users:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form, 'user': request.user})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()
            
            # Send email with OTP
            subject = 'Password Reset OTP'
            message = f'Your OTP for password reset is: {otp}'
            from_email = 'your_email@example.com'  # Update this
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            
            # Encode user id
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            
            return redirect('users:reset_password', uidb64=uidb64, token=token)
        except CustomUser.DoesNotExist:
            messages.error(request, 'No user found with this email address.')
    return render(request, 'users/forgot_password.html')

def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            otp = request.POST.get('otp')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            
            if otp == user.otp:
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.otp = None  # Clear the OTP
                    user.save()
                    messages.success(request, 'Password has been reset successfully.')
                    return redirect('users:login')
                else:
                    messages.error(request, 'Passwords do not match.')
            else:
                messages.error(request, 'Invalid OTP.')
        return render(request, 'users/reset_password.html')
    else:
        messages.error(request, 'The reset link is invalid or has expired.')
        return redirect('users:forgot_password')


# def login_and_register(request):
#     form = CustomUserCreationForm()

#     if request.method == 'POST':
#         if 'register' in request.POST:
#             form = CustomUserCreationForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 django_login(request, user)
#                 return redirect('home')
#             else:
#                 # Instead of a generic message, we'll let the template handle displaying specific errors
#                 pass
#         elif 'login' in request.POST:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 django_login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password')

#     return render(request, 'users/login.html', {'form': form})