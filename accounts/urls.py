from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import redirect
# from polkadot.settings import LOGIN_REDIRECT_URL
from .import views

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html", success_url = '/'), name="login"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile'),
    path("edit/<int:user_id>", views.edit, name='edit'),
    path("update/<pk>", views.UpdateProfileView.as_view(), name='update')
]