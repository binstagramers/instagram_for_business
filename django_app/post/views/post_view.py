from django.contrib.auth import get_user_model
from django.shortcuts import render

from ..models import Post

User = get_user_model()


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)
