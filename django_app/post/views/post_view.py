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
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            Post.objects.create(
                author=request.user,
                photo=photo,
            )
        return redirect('post:post_list')
    elif request.method == 'GET':
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'post/post_create.html', context)
