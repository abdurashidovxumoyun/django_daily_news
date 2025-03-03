from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('single-post/<slug:slug>', single_post.as_view(), name='single-post'),
    path('about/', about.as_view(), name='about'),
    path('author/', author.as_view(), name='author'),
    path('search/', search.as_view(), name='search'),
    path('contact/', contact.as_view(), name='contact'),
    path('error/', error.as_view(), name='error'),
    path('login/', login.as_view(), name='login'),
    path('register/', register.as_view(), name='register')
]
