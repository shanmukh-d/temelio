
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserPermissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permissions = models.ManyToManyField('Permissions', related_name='users')
    
class Permissions(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }