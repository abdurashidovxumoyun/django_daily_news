from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('single-post/', single_post, name='single-post'),
    path('about/', about, name='about'),
    path('author/', author, name='author'),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
    path('error/', error, name='error'),
    path('login/', login, name='login'),
    path('register/', register, name='register')
]
