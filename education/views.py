import random

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, "education/index.html")


def reading(request):
    if request.user.is_authenticated:
        reading_data = Reading.objects.filter(is_published=True)
        if len(reading_data) == 0:
            return redirect("reading", 1)

        paginator = Paginator(reading_data, 1)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)

        return render(
            request,
            "education/reading.html",
            {"reading_data": page_object},
        )
    else:
        return redirect("register")


def math(request, math_id):
    try:
        math_data = Math.objects.get(pk=math_id)
        award = [
            "Молодец!",
            "Прекрасно!",
            "Великолепно!",
            "Продолжай в том же духе!",
            "Очень хорошо!",
            "Двигайся дальше!",
            "У тебя хорошо получается!",
        ]
        reward = [
            "Неправильно",
            "Попробуй еще раз",
            "У тебя получится",
            "Подумай еще раз",
            "Неверный ответ",
        ]
        if request.user.is_authenticated:
            form = MathForm(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    try:
                        pass
                    except:
                        form.add_error(None, "Произошла ошибка")
            return render(
                request,
                "education/math.html",
                {
                    "math_data": math_data,
                    "math_result": {"integer": math_data.integer1 + math_data.integer2},
                    "award": random.choice(award),
                    "form": form,
                    "math_id": math_id,
                    "reward": random.choice(reward),
                },
            )
        else:
            return redirect("register")
    except:
        return redirect("math", 1)


def world_around(request):
    if request.user.is_authenticated:
        category_data = Category.objects.all()
        return render(
            request, "education/world_around.html", {"category_data": category_data}
        )
    else:
        return redirect("register")


def world_around_all(request, cat_slug):
    world_around_data = World_around.objects.filter(
        category__slug=cat_slug, is_published=True
    )
    category_data = Category.objects.filter(slug=cat_slug)

    paginator = Paginator(world_around_data, 2)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    return render(
        request,
        "education/world_around_all.html",
        {"world_around_data": page_object, "category_data": category_data},
    )


def world_around_post(request, cat_slug, world_around_slug):
    world_around_data = World_around.objects.filter(slug=world_around_slug)
    return render(
        request,
        "education/world_around_post.html",
        {"world_around_data": world_around_data},
    )


def pageNotFound(request, exception):
    return render(request, "education/page404.html", status=404)


# Регистрация пользователя
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "education/register.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


# Вход в учетную запись
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "education/login.html"

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy("index")


# Выход пользователя из учетной записи
def logout_user(request):
    logout(request)
    return redirect("login")


# Профиль пользователя на сайте
def profile(request):
    if request.user.is_authenticated:
        return render(request, "education/profile.html")
    else:
        raise Http404()


@login_required
def add_world_around(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddWorldAroundForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("world_around")
        else:
            form = AddWorldAroundForm()
        return render(request, "education/add_world_around.html", {"form": form})
    else:
        raise Http404()


class EditProfile(generic.UpdateView):
    model = UserProfile
    template_name = "education/edit_profile.html"
    fields = ["avatar"]
    success_url = reverse_lazy("profile")


class CreateProfile(generic.CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'education/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def additional(request):
    if request.user.is_authenticated:
        return render(request, "education/additional.html")
    else:
        raise Http404()


def support(request):
    return render(request, "education/support.html")


def comments(request):
    if request.user.is_authenticated:
        comments_data = Comments.objects.all()
        comments_count = len(comments_data)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect("comments")
        else:
            form = CommentForm()

        return render(
            request,
            "education/comments.html",
            {
                "form": form,
                "comments_data": comments_data,
                "comments_count": comments_count,
            },
        )
    else:
        raise Http404()
