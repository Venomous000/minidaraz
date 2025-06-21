# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, SuperAdminLoginForm, AdminUserCreationForm
from .models import User
from .models import Admin, AdminUser
from django.contrib.auth.decorators import login_required
from accounts.decorators import superadmin_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password





def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or cart/dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    error = None
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid credentials'
    return render(request, 'accounts/login.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


# def admin_login_view(request):
#     form = AdminLoginForm(request.POST or None)
#     error = None
#     if request.method == 'POST' and form.is_valid():
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         try:
#             admin = Admin.objects.get(email=email, password=password)
#             request.session['admin_logged_in'] = True
#             request.session['admin_email'] = admin.email
#             return redirect('admin-dashboard')  # define later
#         except Admin.DoesNotExist:
#             error = "Invalid admin credentials"
#     return render(request, 'accounts/admin_login.html', {'form': form, 'error': error})



def superadmin_login_view(request):
    form = SuperAdminLoginForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        raw_password = form.cleaned_data['password']

        try:
            admin = Admin.objects.get(email=email, role='superadmin')
            if check_password(raw_password, admin.password):
                request.session['superadmin_logged_in'] = True
                request.session['superadmin_id'] = admin.id
                return redirect('superadmin-dashboard')
            else:
                error = "Incorrect password"
        except Admin.DoesNotExist:
            error = "SuperAdmin not found."

    return render(request, 'accounts/superadmin_login.html', {'form': form, 'error': error})



def superadmin_dashboard_view(request):
    if not request.session.get('superadmin_id'):
        return redirect('superadmin-login')
    return render(request, 'accounts/superadmin_dashboard.html')

def superadmin_logout_view(request):
    logout(request)
    return redirect('superadmin-login')  # or wherever you want to redirect

@login_required
def home_view(request):
    return render(request, 'home.html')



@superadmin_required
def add_admin_user_view(request):
    superadmin_id = request.session.get('superadmin_id')
    if not superadmin_id:
        return redirect('superadmin-login')

    superadmin = Admin.objects.get(id=superadmin_id)

    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            new_admin_user = form.save(commit=False)
            new_admin_user.superadmin = superadmin
            new_admin_user.save()
            return redirect('superadmin-dashboard')
    else:
        form = AdminUserCreationForm()

    return render(request, 'accounts/add_admin_user.html', {'form': form})


@superadmin_required
def superadmin_dashboard_view(request):
    superadmin_id = request.session.get('superadmin_id')
    if not superadmin_id:
        return redirect('superadmin-login')

    superadmin = Admin.objects.get(id=superadmin_id)
    form = AdminUserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_admin_user = form.save(commit=False)
        new_admin_user.superadmin = superadmin
        new_admin_user.save()
        return redirect('superadmin-dashboard')

    all_admin_users = AdminUser.objects.filter(superadmin=superadmin)

    return render(request, 'accounts/superadmin_dashboard.html', {
        'form': form,
        'admin_users': all_admin_users,
    })
