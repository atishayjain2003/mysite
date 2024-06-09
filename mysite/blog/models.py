from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    





    options=(('draft','Draft'),
             ('published','Published'),
             )
    title=models.CharField(max_length=250)
    excerpt=models.TextField(null=True)
    slug=models.SlugField(max_length=250, unique_for_date='publish')
    publish=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    #if a user is deleted then all the post related to that user will be deleted 
    # this is the function of delete=models.cascade
    content=models.TextField(default=' ')
    status=models.CharField(max_length=10, choices=options, default='draft')
    #makemigrations is used to prepare the model to make changes to the database
    #migrate is used to make the changes to the database
   

    class Meta:
        ordering = ('-publish',)
    # for ordering the blogs by date
    
    def __str__(self):
        return self.title
    #used to display title on django admin site
    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

