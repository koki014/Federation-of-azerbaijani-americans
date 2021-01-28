from django.db.models.signals import pre_save
from django.conf import settings
from django.dispatch import receiver
from django.utils.timezone import now
from django.core.mail import send_mail
from .models import DonationUser


# @receiver(pre_save, sender=DonationUser)
# def create_contact(sender,  instance, **kwargs):
#     membership = 
#     print(membership, 'salam')

#     users_data = f'''
#         salam
#     '''
#     print(users_data)
#     subject = "subject"
#     your_email = 'husubeyli@gmail.com'
#     send_mail(subject, users_data, settings.EMAIL_HOST_USER, [instance.email,])



@receiver(pre_save, sender=DonationUser)
def create_profile(sender, instance, created, **kwargs):
    pass
    # if created:
    #     profile = DonationUser()
    #     membership_id_in_base = DonationUser.objects.filter(membership_id=instance.membership_id)
    #     if not membership_id_in_base:
    #         profile.membership_id = f'{instance.membership_id}{instance.id}'
    #     subject = "subject"
    #     print(profile.membership_id, 'alala')
    #     send_mail(subject, instance.membership_id, settings.EMAIL_HOST_USER, [instance.email,])
    #     profile.save()


