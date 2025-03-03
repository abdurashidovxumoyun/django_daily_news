from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


class home(TemplateView):
    template_name = 'pages/home.html'
   

class single_post(TemplateView):
    model = Post
    template_name='pages/single-post.html'
    context_object_name = 'posts'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    

class about(TemplateView):
    template_name='pages/about-us.html'
    

class author(TemplateView):
    template_name='pages/author.html'

class search(TemplateView):
    template_name='pages/search.html'

class contact(TemplateView):
    template_name='pages/contact.html'

class error(TemplateView):
    template_name='pages/error.html'

class login(TemplateView):
    template_name='pages/login.html'

class register(TemplateView):
    template_name='pages/register.html'