from django.shortcuts import render
from django.core.mail import send_mail
from .models import info
from django.contrib import messages
from django.conf import settings
# Create your views here.

def contact(request):
    data = info.objects.first()

    if request.method == 'POST':
        sender_email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if sender_email and subject and message is not None:
          email = settings.EMAIL_HOST_USER  # Set the recipient email address

          sender_subject = f"From:{sender_email}\t,{subject}"

          send_mail(
            sender_subject,
            message,
            email,
            [email],
            fail_silently=False,

           )
          messages.success(request,'Your Message Sent Successfully')
          return render(request,'contact/contact.html',{})
        else:
           messages.error(request,'there was an error sending the message! ')
    return render(request, 'contact/contact.html', {'data': data})
    