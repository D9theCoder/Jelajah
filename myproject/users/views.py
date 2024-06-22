from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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