from django.contrib import admin
from . import models
# Register your models here.

class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['name','email','gender']

class AccountModelAdmin(admin.ModelAdmin):
    list_display=['customer_id','accno','account_type',"account_owner",'account_status']

admin.site.register(models.CustomerModel,CustomerModelAdmin)
admin.site.register(models.AccountModel,AccountModelAdmin)