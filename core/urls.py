from django.urls import path

from .views import (
    ContactView,
    SubscriberView
)

app_name = 'core'


urlpatterns = [
<<<<<<< HEAD
    path("", HomePageView.as_view(), name="index")
=======
    path("", ContactView.as_view(), name="index"),
    path("", SubscriberView.as_view(), name='index')
>>>>>>> 118a1708e4ad598fe1bf563510c32302a2c955fa
]