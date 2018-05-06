from django.contrib.auth.admin import UserAdmin

from auth.forms import UserCreateForm


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name', 'last_name',)}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'email',
                       'is_staff', 'is_superuser', 'is_active'),
        }),
        (None, {
            'classes': ('wide',),
            'fields': ('groups',)
        })
    )
