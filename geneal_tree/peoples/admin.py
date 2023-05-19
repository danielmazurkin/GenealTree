from django.contrib import admin
from peoples.models import People
from bios.models import BioPeople
from django.conf import settings
from django.utils.safestring import mark_safe


@admin.register(People)
class AdminPeople(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'sex', 'link_profile', )
    search_fields = ('people__first_name', 'people__last_name', 'people__surname', )

    @admin.display(description='Профиль человека')
    def link_profile(self, obj) -> str:
        return mark_safe(
            f"<a href='{settings.SITE_URL}/profiles/profile/{obj.pk}'> Профиль человека </a>"
        )


@admin.register(BioPeople)
class AdminBioPeople(admin.ModelAdmin):
    search_fields = ('people__first_name', 'people__last_name', 'people__surname', )
    list_display = ('people', )

