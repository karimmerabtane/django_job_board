from django.shortcuts import get_object_or_404, redirect, render
from .forms import CityForm , SingupForm , ProfileForm, UserForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.


def singup(request):
    if request.method =='POST':
        form = SingupForm(request.POST )
        if form.is_valid() :
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username,password= password) 
            login(request,user)
            return redirect('/accounts/profile')

    else:
        form = SingupForm()
    context = {
        'form':form
    }
    return render(request, 'registration/singup.html', context)
    

def profile(request):
    profile = Profile.objects.get(user = request.user)
    user    = request.user
    context={
     'profile':profile,
     'user'   : user,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    user   = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method=='POST':
        userform = UserForm(request.POST,request.FILES,instance=user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('/accounts/profile/')
    else:
        userform = UserForm(instance = user)
        profileform = ProfileForm(instance=profile)
    context = {
        'userform':userform,
        'profileform':profileform , 
        'user':user,
        'profile':profile,
    }
    return render(request, 'edit_profile.html', context)
    

def add_new_city(request):
    if request.method =='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/edit_profile')
    else:
        form = CityForm()
    form = CityForm()
    context = {
        'form':form ,
    }
    return render(request, 'add_new_city.html', context)
    
