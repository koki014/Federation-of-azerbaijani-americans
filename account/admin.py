from django.contrib import admin
from .models import DonationUser


@admin.register(DonationUser)
class DonationUser(admin.ModelAdmin):
    readonly_fields=('membership_id',)
    ordering = ('email',)
    search_fields = ('full_name',)