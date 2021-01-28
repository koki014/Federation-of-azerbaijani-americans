from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    last_name = None
    first_name = None
    full_name = models.CharField(_('full name'), max_length=80, blank=False, null=False )
    email = models.EmailField(_('email address'), unique=True)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=30, blank=False, null=False)
    citizenship = models.CharField(_('citizenship'), max_length=225, blank=False, null=False )
    education = models.CharField(_('education'), max_length=225, blank=False, null=False)
    current = models.CharField(_('current'), max_length=225, blank=False, null=False)
    permoment = models.CharField(_('permoment'), max_length=225, blank=False, null=False)
    memeber_of_ngo = models.CharField(_('memeber of ngo'), max_length=225, blank=False, null=False)
    usa_year = models.IntegerField(_('usa year'), blank=False, null=False)
    reasons = models.TextField(_('reasons'), blank=False, null=False)
    mention = models.TextField(_('mention'), blank=False, null=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    bjects = UserManager()

    def __str__(self):
        return self.email