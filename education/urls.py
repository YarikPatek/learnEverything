from django.template.defaulttags import comment
from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("profile/", profile, name="profile"),
    path("reading/", reading, name="reading"),
    path("math/<int:math_id>/", math, name="math"),
    path("world_around/", world_around, name="world_around"),
    path("world_around/<slug:cat_slug>/", world_around_all, name="world_around_all"),
    path(
        "world_around/<slug:cat_slug>/<slug:world_around_slug>/",
        world_around_post,
        name="world_around_post",
    ),
    path("add_world_around/", add_world_around, name="add_world_around"),
    path("<int:pk>/edit_profile/", EditProfile.as_view(), name="edit_profile"),
    path("additional", additional, name="additional"),
    path("support", support, name="support"),
    path("comments", comments, name="comments"),
    path("create_profile/", CreateProfile.as_view(), name="create_profile"),
]
