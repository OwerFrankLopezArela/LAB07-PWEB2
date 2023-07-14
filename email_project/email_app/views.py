from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EmailForm
from .models import Email

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save()
            send_mail(
                email.subject,
                email.message,
                'your_email@example.com',  # Reemplaza con tu dirección de email
                [email.recipient],
                fail_silently=False,
            )
            email.sent = True
            email.save()
            return redirect('success')
    else:
        form = EmailForm()
    return render(request, 'email_app/email.html', {'form': form})

def success(request):
    return render(request, 'email_app/success.html')
