from django.contrib import admin
from personsManager.models import Contact,Profile

#admin.site.register(Profile)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	exclude = ['added_by',]


admin.site.register(Profile)

