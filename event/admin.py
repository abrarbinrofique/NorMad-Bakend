from django.contrib import admin
from .models import Travel,Review,sms

# Register your models here.

class travelevent(admin.ModelAdmin):
    list=['location','traveldate','time','Description','cost','image','people_limit']


admin.site.register(Travel,travelevent)
admin.site.register(Review)
admin.site.register(sms)
