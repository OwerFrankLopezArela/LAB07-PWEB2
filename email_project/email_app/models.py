from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=100)
    recipient = models.EmailField()
    message = models.TextField()
    sent = models.BooleanField(default=False)
