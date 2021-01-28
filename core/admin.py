from core.models import Contact
from django.contrib import admin
from .models import Contact, Subscriber
# Register your models here.
admin.site.register([Contact, Subscriber])