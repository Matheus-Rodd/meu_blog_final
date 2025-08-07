from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'now': timezone.now()  
    })