from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """ Custom User Admin """

    custom_fieldsets = (
        ('Custom', {
            "fields": (
                'avatar',
                'bio',
                'birthdate',
                'currency',
                'gender',
                'language',
                'superhost',
                'login_method',
            ),
        }),
    )
    fieldsets = UserAdmin.fieldsets + custom_fieldsets

    list_filter = UserAdmin.list_filter + ('superhost',)

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
        'email_verified',
        'email_secret',
        'login_method',
    )
