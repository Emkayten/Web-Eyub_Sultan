from django.contrib import admin
from .models import UserProfile, Role

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_roles', 'failed_attempts', 'lockout_until')
    list_filter = ('roles',)

    def display_roles(self, obj):
        return ", ".join(role.name for role in obj.roles.all())
    display_roles.short_description = 'Rollen'

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
