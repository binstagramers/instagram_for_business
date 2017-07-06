from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from ..form import PostForm
from ..models import Post

User = get_user_model()


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(author=request.user)
        return redirect('post:post_list')
