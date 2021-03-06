from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class FarmFoodUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_producer', 'is_consumer')
    list_filter = ('is_staff', 'is_superuser', 'groups', 'is_producer', 'is_consumer')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_producer', 'is_consumer')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_producer', 'is_consumer'),
        }),
    )

    readonly_fields = ('date_joined', 'last_login')
