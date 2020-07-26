from django.urls import include, path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('singup/', views.singup, name='singup'),
    path('profile/',views.profile , name = 'profile'),
    path('edit_profile/',views.edit_profile , name ='edit_profile'),
    path('add_new_city', views.add_new_city, name='add_new_city'),
   

]
