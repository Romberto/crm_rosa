from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            if field == 'username':
                self.fields[field].widget.attrs['placeholder'] = 'login'
            elif field == 'password':
                self.fields[field].widget.attrs['placeholder'] = 'password'

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Пользователя с таким логином и паролем не существует")
    #     return self.cleaned_data