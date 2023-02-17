from django.shortcuts import render
from . models import Featured, Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    if request.method == 'POST':
        message_subject = request.POST.get('subject')
        message_name = request.POST.get('Name')
        message_email = request.POST.get('Email')
        message_message = request.POST.get('message')

        contact = Contact(subject=message_subject, name=message_name, email=message_email, message=message_message )
        contact.save()        

        send_mail(
            message_subject,
            message_message,
            message_email,
            [settings.EMAIL_HOST_USER]
        )
        
        
        messages.success(request, f"{message_name} Your message has been received. We will get back to you shortly.")

    return render(request, "contact.html")

def portfolio(request):
    portfolio = Featured.objects.all()
    context = {'portfolio': portfolio}
    return render(request, "portfolio.html", context)
    

    
