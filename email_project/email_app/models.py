from django.db import models

class Email(models.Model):
    asunto = models.CharField(max_length=100)
    destinatario = models.EmailField()
    mensaje = models.TextField()
    sent = models.BooleanField(default=False)
