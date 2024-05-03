from django.db import models

# Create your models here.

class Nonprofit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(default="")
    email = models.EmailField(unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'email': self.email
        }   

class SentEmails(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_from = models.EmailField(db_index=True)
    sent_to = models.EmailField(db_index=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # having email feilds instead of foreign key to keep it simple and scalable in the future as these can be used only for analytics

    def to_dict(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'message': self.message,
            'sent_from': self.sent_from,
            'sent_to': self.sent_to,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }