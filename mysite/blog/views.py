from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    all_posts=Post.objects.all()






    return render(request, 'index.html', {'posts':all_posts})
#the templates folder is inside the app

