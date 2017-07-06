from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from .form import SignUpForm

User = get_user_model()


def create_user(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            image_profile = form.cleaned_data['image_profile']
            User.objects.create(
                username=username,
                password=password,
                image_profile=image_profile,
            )
            return redirect('post:post_list')

    elif request.method == 'GET':
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'member/create_user.html', context)
