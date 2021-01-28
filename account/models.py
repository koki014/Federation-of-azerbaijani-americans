import uuid
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager


class DonationUser(models.Model):
    full_name = models.CharField(_('full name'), max_length=80 )
    membership_id = models.CharField(_("Membership id"), max_length=50, default='', null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    birthday = models.DateField(_("Birthday"), auto_now_add=False, auto_now=False)
    phone_number = models.CharField(_('phone number'), max_length=30)
    citizenship = models.CharField(_('citizenship'), max_length=225 )
    education = models.CharField(_('education'), max_length=225)
    current = models.CharField(_('current'), max_length=225)
    permoment = models.CharField(_('permoment'), max_length=225)
    member_of_ngo = models.CharField(_('member of ngo'), max_length=225)
    usa_year = models.IntegerField(_('usa year'), null=True)
    reasons = models.TextField(_('reasons'))
    mention = models.TextField(_('mention'))


    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        """Meta definition for Contact."""
        verbose_name = 'Donation User'
        verbose_name_plural = 'Donation Users'

    def save(self, *args, **kwargs):
        raw_id = uuid.uuid1()
        raw_membership_id = str(raw_id.int)[:6]
        self.membership_id = f'{raw_membership_id}{self.id}'
        print(self.id, 'id-ss')
        send_mail('subject', f'This is ypu membership id {self.membership_id}', 'tech.academy.docker@gmail.com', [self.email,])
        super(DonationUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email