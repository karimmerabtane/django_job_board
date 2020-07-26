from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg   = f"bonjour karim i am {name},i have email {email} \n\n"  \
                       f"  {message}"
            send_mail(subject, msg, 'karimbiologie@gmail.com', ['karim.sniper88@gmail.com'])
            return redirect('/jobs')
    else:
        form = ContactForm()
    context = {
       'form':form, 
    }
    return  render(request, 'contact.html', context)
    
