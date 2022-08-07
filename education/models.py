import ordering as ordering
import slug as slug
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Math(models.Model):
    integer1 = models.IntegerField(verbose_name="Первое число")
    integer2 = models.IntegerField(verbose_name="Второе число")

    class Meta:
        verbose_name = "Математика"
        verbose_name_plural = "Математика"
        ordering = ["id"]

    def __str__(self):
        return "Обьект математика"


class Reading(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Текст для чтения")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(default=True, verbose_name="Показать на сайте")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Чтение"
        verbose_name_plural = "Чтение"
        ordering = ["id"]


class World_around(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    content = models.TextField(blank=True, verbose_name="Текст для чтения")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(default=True, verbose_name="Показать на сайте")
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Окружающий мир"
        verbose_name_plural = "Окружающий мир"
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("category", kwargs={"world_around_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Фотография", null=True
    )
    description = models.TextField(
        blank=True, verbose_name="Описание категории", null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Аватар пользователя", blank=True
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Дополнение пользовательской базы"
        verbose_name_plural = "Дополнение пользовательской базы"

    def get_absolute_url(self):
        return reverse('profile')



class Comments(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    content = models.TextField(blank=True, verbose_name="Текст комментария")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(
        default=True, verbose_name="Показать комментарий на сайте"
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["id"]
