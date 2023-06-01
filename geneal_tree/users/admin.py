from django.contrib import admin
from users.models import AllowedUser


@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    """Разрешенный пользователь."""
    pass

