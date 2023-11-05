from django.urls import path
from .views import *

urlpatterns = [
    path('', fullcontent, name='home'),
    path('contact/', contact, name='contact'),
    path('category/', CategoryVilla.as_view(), name='category'),
    path('category/<str:slug>', GetCategory.as_view(), name='category'),
    path('detail/<str:slug>', GetVilla.as_view(), name='detail'),
    path('add_villa/', add_villa, name='add-villa'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
 ]
