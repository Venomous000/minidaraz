from django.urls import path
from .views import register_view, login_view, logout_view, superadmin_login_view, superadmin_logout_view, superadmin_dashboard_view, add_admin_user_view
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('admin-login/', admin_login_view, name='admin-login'),
    path('superadmin-login/', superadmin_login_view, name='superadmin-login'),
    path('superadmin-dashboard/', superadmin_dashboard_view, name='superadmin-dashboard'),
    path('add-admin-user/', add_admin_user_view, name='add-admin-user'),
    path('superadmin/add-admin/', add_admin_user_view, name='add-admin-user'),
    path('superadmin/logout/', superadmin_logout_view, name='superadmin-logout'),

]