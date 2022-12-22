from django.contrib import admin
from mediainstall.models import User_Profile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'technologies', 'email', 'display_picture']


admin.site.register(User_Profile, UserProfileAdmin)