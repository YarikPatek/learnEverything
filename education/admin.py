from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from education.models import *


class ReadingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "get_html_photo", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_editable = ("is_published",)
    list_filter = ("is_published", "time_create")

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Фотография"


class World_aroundAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "time_create",
        "get_html_photo",
        "is_published",
        "category",
    )
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_editable = ("is_published",)
    list_filter = ("is_published", "time_create", "category")
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        "title",
        "slug",
        "category",
        "content",
        "photo",
        "time_create",
        "is_published",
    )
    readonly_fields = ("time_create",)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Фотография"


class MathAdmin(admin.ModelAdmin):
    list_display = ("id", "integer1", "integer2")
    list_display_links = ("id",)
    list_editable = ("integer1", "integer2")


class Category_admin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description", "get_html_photo")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_html_photo.short_description = "Аватар"


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "get_html_photo")

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_html_photo.short_description = "Аватар"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content", "time_create", "is_published")
    list_display_links = ("id", "user", "content")
    search_fields = ("content",)
    list_filter = ("is_published", "time_create", "user")
    list_editable = ("is_published",)


admin.site.register(Reading, ReadingAdmin)
admin.site.register(World_around, World_aroundAdmin)
admin.site.register(Category, Category_admin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Math, MathAdmin)
admin.site.register(Comments, CommentsAdmin)
