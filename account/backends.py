from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .models import DonationUser

class DonationUserBackend(ModelBackend):
    def authenticate(self, membership_id=None):
        try:
            user = User.objects.get(membership_id=membership_id)
            if user:
                return user
        except User.DoesNotExist:
            return None 
            