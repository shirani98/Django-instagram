from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from accounts.forms import UserChangeForm, UserCreationForm
from .models import MyUser
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'phone','is_admin')
    list_filter = ('is_admin','is_active')
    fieldsets = (
        ('Main', {'fields': ('email','username','phone', 'password')}),
        ('Personal info', {'fields': ('date_of_birth','firstname','lastname',)}),
        ('Permissions', {'fields': ('is_admin','is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
