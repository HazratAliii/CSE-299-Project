from django.urls import path
from . import views   

urlpatterns = [
    path("", views.tregister, name="user-register"),
    path("profile/", views.profile, name="user-profile"),
    path("register/", views.register_sub, name="register-sub"),
    path("login/", views.login, name="user-login"),
    path("login_sub/", views.login_sub, name="user-login_sub"),
    path("hotels/", views.hotels, name="user-hotels"),
    path("hotel_info_sub/", views.hotel_info_sub, name="user-hotels_info"),
    path("hotel_page/", views.hotel_page, name="user-hotel_page"),
]