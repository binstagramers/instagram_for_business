from django import forms

from .models import User


class SignUpForm(forms.Form):
    username = forms.CharField(
        help_text='Signup help text test',
        widget=forms.TextInput
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )
    image_profile = forms.ImageField(
        widget=forms.FileInput(
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist'
            )
        return username

    def clean_password2(self):
        # password1과 password2를 비교하여 같은지 검증
        # password2필드에 clean_<fieldname>을 재정의한 이유는,
        #   cleaned_data에 password1이 이미 들어와 있어야 하기 때문
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Password mismatch',
            )
        return password2
