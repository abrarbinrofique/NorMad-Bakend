from django.contrib import admin
from .models import chatmodel,sms
# Register your models here.
admin.site.register(sms)
admin.site.register(chatmodel)