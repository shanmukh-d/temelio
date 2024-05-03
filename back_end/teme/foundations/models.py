from django.db import models

# Create your models here.
class Foundation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }