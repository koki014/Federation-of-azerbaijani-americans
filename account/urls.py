from django.urls import path, include, re_path
from .views import RegisterCreateView

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register")
]