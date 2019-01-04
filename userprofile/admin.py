from django.contrib import admin
from mainsite.forms import UserRegistrationForm
from .models import AuthorProfile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    model = AuthorProfile
    list_display = ['email', 'username',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('author_image', )}),)

admin.site.register(AuthorProfile, CustomUserAdmin)