from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    template_name = 'pages/home.html'
    return render(request=request, template_name=template_name)

def single_post(request):
    template_name = 'pages/single-post.html'
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request=request, template_name=template_name, context=context)

def about(request):
    template_name='pages/about-us.html'
    return render(request=request, template_name=template_name)

def author(request):
    return render(request=request, template_name='pages/author.html')

def search(request):
    return render(request=request, template_name='pages/search.html')

def contact(request):
    return render(request=request, template_name='pages/contact.html')

def error(request):
    return render(request=request, template_name='pages/error.html')

def login(request):
    return render(request=request, template_name='pages/login.html')

def register(request):
    return render(request=request, template_name='pages/register.html')