from django.contrib.auth.models import User
from common.models import UserPermissions

def get_user_from_username(username: str) -> User:
    return User.objects.filter(username=username).first()

def check_if_user_has_permission(user: User, permission_name: str) -> bool:
    "checks if the user has the permission or not"
    return UserPermissions.objects.filter(user=user, permissions__name=permission_name).exists()