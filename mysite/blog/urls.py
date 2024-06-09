from django.urls import path
from . import views

app_name='blog'
#this should be same as namespace

urlpatterns = [
    path('', views.home,  name='homepage'),
    #blog is the base, anything in the quotes that is put up at the browser will show index.html only
    path('<slug:post>/', views.post_single, name='post_single'),
    
]
