from django.contrib import admin

# Register your models here.

from common import models

admin.site.register(models.UserPermissions)
admin.site.register(models.Permissions)