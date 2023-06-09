from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe
from peoples.models import People


@admin.register(People)
class AdminPeople(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'sex', 'link_profile', )
    search_fields = ('people__first_name', 'people__last_name', 'people__surname', )
    exclude = ('owner_user', )

    @admin.display(description='Профиль человека')
    def link_profile(self, obj) -> str:
        return mark_safe(
            f"<a href='{settings.SITE_URL}/profiles/profile/{obj.pk}'> Профиль человека </a>"
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Переопределяем данные в выпадающем списке внешнего ключа."""
        if db_field.name == "mother" or db_field.name == "father" or db_field.name == "marriage":
            kwargs["queryset"] = People.objects.filter(owner_user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        """Переопределение сохранения модели для создания многопользовательского режима."""
        obj.owner_user = request.user
        obj.save()

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)
