from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    all_posts=Post.objects.filter(status='published')






    return render(request, 'index.html', {'posts':all_posts})
#the templates folder is inside the app

def post_single(request, post):
    post=get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post':post})
def homex(request):
    return render(request, "home1.html")



