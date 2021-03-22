from django.urls import path
from . import views   

urlpatterns = [
    path("", views.tregister, name="user-register"),
    path("profile/", views.profile, name="user-profile"),
    path("register/", views.register_sub, name="register-sub"),
]