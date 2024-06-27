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
        


class CustomUserChangeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            if field != 'password':
                self.fields[field].widget.attrs['placeholder'] = getattr(self.instance, field)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            return self.instance.password
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        
        if not username:
            self.add_error('username', "Username cannot be empty.")
        if not email:
            self.add_error('email', "Email cannot be empty.")
        if not name:
            self.add_error('name', "Name cannot be empty.")
        
        if not any(cleaned_data.values()):
            raise forms.ValidationError("You must change at least one field.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password and not password.startswith('pbkdf2_'):  # Check if it's a new password (not hashed yet)
            user.set_password(password)
        else:
            password = None
        if commit:
            user.save()
        return user

    


    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     password = self.cleaned_data.get('password')
    #     if password != self.instance.password:
    #         user.set_password(password)
    #     if commit:
    #         user.save()
    #     return user

# class ProfileUpdateForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}), required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'name', 'password']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form_input'})

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
