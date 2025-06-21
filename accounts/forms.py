from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, AdminUser

# Sign up system
class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password1', 'password2']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }


# Login system
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# class AdminLoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

# Super Admin Login system
class SuperAdminLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AdminUserCreationForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['name', 'email', 'role', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }