from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class MathForm(forms.Form):
    integer = forms.IntegerField(
        label="Введи сюда свой ответ",
        widget=forms.TextInput(
            attrs={"name": "integer", "id": "integer", "class": "form-control"}
        ),
    )


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )
    first_name = forms.CharField(
        label="Твое имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )
    last_name = forms.CharField(
        label="Твоя фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "floatingInputValue",
                "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
            }
        ),
    )


class AddWorldAroundForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Категория не выбрана"

    class Meta:
        model = World_around
        fields = ["title", "slug", "content", "photo", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "floatingInputValue",
                    "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "floatingInputValue",
                    "style": "width: 300px; height: 50px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
                }
            ),
        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "floatingInputValue",
                    "style": "width: 500px; height: 200px; background: radial-gradient(at top, #FEFFFF, #A7CECC); font-size: 30px; font-weight: bold;",
                }
            )
        }
