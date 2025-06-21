from functools import wraps
from django.shortcuts import redirect

def superadmin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('superadmin_id'):
            return redirect('superadmin-login')
        return view_func(request, *args, **kwargs)
    return wrapper