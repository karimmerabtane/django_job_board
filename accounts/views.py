from django.shortcuts import redirect, render
from .forms import CityForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
# Create your views here.


def singup(request):
    if request.method =='POST':
        form = UserForm(request.POST )
        if form.is_valid() :
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username,password= password) 
            login(request,user)
            return redirect('/accounts/profile')

    else:
        form = UserForm()
    context = {
        'form':form
    }
    return render(request, 'registration/singup.html', context)
    