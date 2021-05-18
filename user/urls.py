from django.urls import path
from . import views   

urlpatterns = [
   
    path("", views.tregister, name="user-register"),
    path("profile/", views.profile, name="user-profile"),
    path("register_sub/", views.register_sub, name="register-sub"),
    path("tourist_register_sub/", views.tourist_register_sub, name="tourist-register-sub"),
    path("login/", views.login, name="user-login"),
    path("login_sub/", views.login_sub, name="user-login_sub"),
    # path("login_sub/<slug:email>", views.login_sub, name="user-login_sub"),
    path("hotels/", views.hotels, name="user-hotels"),
    path("hotel_info_sub/", views.hotel_info_sub, name="user-hotels_info"),
    path("hotel_page/", views.hotel_page, name="user-hotel_page"),
    path("about_us/", views.about_us, name="user-about_us"),
    path("hotel_list/", views.hotel_list, name="user-hotel_list"),
    path("tourist_login/", views.tourist_login, name="user-tourist_login"),
    path("guide_login/", views.guide_login, name="user-guide_login"),
    path("tourist_signup/", views.tourist_signup, name="user-tourist_signup"),
    path("guide_signup/", views.guide_signup, name="user-guide_signup"),
    path("rangamati/", views.rangamati, name="user-rangamati"),
    path("kuakata/", views.kuakata, name="user-kuakata"),
    path("sundarban/", views.sundarban, name="user-sundarban"),
    path("coxsbazar/", views.coxsbazar, name="user-coxsbazar"),
    path("rangamati_sub/<int:pk>", views.rangamati_sub, name="user-rangamati_sub"),
    path("kuakata_sub/<int:pk>", views.kuakata_sub, name="user-kuakata_sub"),
    path("sundarban_sub/<int:pk>", views.sundarban_sub, name="user-sundarban_sub"),
    path("coxsbazar_sub/<int:pk>", views.coxsbazar_sub, name="user-coxsbazar_sub"),
    path("guide_info/", views.guide_info, name="user-guideinfo"),
    path("register_sub/", views.register_sub, name="user-register_sub"),
    path("guide_info/<str:name>", views.guide_info, name = "user-guide_info"),
    path("profile2/<int:pk>", views.profile2, name = "user-profile2"),
    path("profile2_sub/<int:pk>", views.profile2_sub, name = "user-profile2_sub"),
    
]