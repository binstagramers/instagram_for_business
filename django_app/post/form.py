from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'photo',
        ]


class PaymentsForm(forms.Form):
    price = forms.IntegerField()
