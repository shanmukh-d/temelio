from django.http import HttpResponseForbidden
from functools import wraps
from django.contrib.auth.models import User
from common import dal

import json

def permission_required(permission_name: str):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            if dal.check_if_user_has_permission(request.user, permission_name):
                return view_func(self, request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        return wrapper
    return decorator

def login_required(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_name = json.loads(request.body.decode('utf-8')).get('user_name')
        else:
            user_name = request.GET.get('user_name')
        
        if not user_name:
            return HttpResponseForbidden()
        
        user = User.objects.filter(username=user_name).first()
        if not user:
            return HttpResponseForbidden()
        
        request.user = user
        return view_func(self, request, *args, **kwargs)
    return wrapper