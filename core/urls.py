from django.urls import path

from .views import (
    ContactView,
    SubscriberView
)

app_name = 'core'


urlpatterns = [
    path("", ContactView.as_view(), name="index"),
    path("", SubscriberView.as_view(), name='index')
]