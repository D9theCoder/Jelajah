from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    agree_to_terms = forms.BooleanField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ["username", "email", "name", "password1", "password2"]
        
class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form_input'})

# class ProfileUpdateForm(forms.ModelForm):
#     username = forms.CharField(max_length=100, required=True)
#     name = forms.CharField(max_length=100, required=True)
#     password = forms.CharField(widget=forms.PasswordInput(), required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'name', 'password']

# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class UpdateProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
#     bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

#     class Meta:
#         model = Profile
#         fields = ['avatar', 'bio']
