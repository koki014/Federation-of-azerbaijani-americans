from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget
from django.forms import ModelForm
from django.contrib import admin
from .models import DonationUser, Message


class DonationUserModelForm(ModelForm):
    class Meta:
        model = DonationUser
        fields = "__all__"
        widgets = {
            "is_active": DjangoToggleSwitchWidget(round=True, klass="django-toggle-switch-success"),
        }

class DonationUserAdmin(admin.ModelAdmin):
    form = DonationUserModelForm

    readonly_fields = ('membership_id',)
    ordering = ('email',)
    search_fields = ('full_name',)



admin.site.register(DonationUser, DonationUserAdmin)
admin.site.register(Message)