from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    last_name = None
    first_name = None
    full_name = models.CharField(_('full name'), max_length=80 )
    email = models.EmailField(_('email address'), unique=True)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=30)
    citizenship = models.CharField(_('citizenship'), max_length=225 )
    education = models.CharField(_('education'), max_length=225)
    current = models.CharField(_('current'), max_length=225)
    permoment = models.CharField(_('permoment'), max_length=225)
    member_of_ngo = models.CharField(_('member of ngo'), max_length=225)
    usa_year = models.IntegerField(_('usa year'), null=True)
    reasons = models.TextField(_('reasons'))
    mention = models.TextField(_('mention'))


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    bjects = UserManager()

    def __str__(self):
        return self.email