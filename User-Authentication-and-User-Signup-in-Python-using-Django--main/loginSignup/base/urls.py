from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import authView, home
from .views import home, upload_screenshot

urlpatterns = [
    # Login and Registration URLs

 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 path('upload_screenshot/', upload_screenshot, name='upload_screenshot'),
]

