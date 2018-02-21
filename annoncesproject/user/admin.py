from django.contrib import admin
from user.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from annonces.models import Annonce

class AnnonceInline(admin.TabularInline):
    model = Annonce



class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    #fields= ('birth',)
    fieldsets = ((
        None, {'fields':('birth', 'phone')}),
    )


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)

admin.site.register(User,  UserAdmin)
##admin.site.register(Profile, ProfileAdmin)