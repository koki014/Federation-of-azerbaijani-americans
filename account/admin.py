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

# class MessageAdmin(admin.ModelAdmin):
#     change_form_template = "admin/send_message.html"

    
#     def response_change(self, request, obj):
#         if "send-message" in request.POST:
#             # subscribers = [i for i in Subscriber.objects.all()]
#             # print(subscribers)
#             # for subscriber in subscribers:
#             # send_mail(obj.subject, obj.content, 'tech.academy.docker@gmail.com', [subscriber.mail])
#             print("nagayrsan")
#         return HttpResponseRedirect("/admin/account/message/")

admin.site.register(DonationUser, DonationUserAdmin)
admin.site.register(Message)