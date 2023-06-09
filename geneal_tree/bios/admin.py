from django.contrib import admin
from bios.models import BioPeople
from peoples.models import People


@admin.register(BioPeople)
class AdminBioPeople(admin.ModelAdmin):
    search_fields = ('people__first_name', 'people__last_name', 'people__surname', )
    list_display = ('people', )
    exclude = ('owner_user', )

    def save_model(self, request, obj, form, change):
        """Переопределение сохранения модели для создания многопользовательского режима."""
        obj.owner_user = request.user
        obj.save()

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Переопределяем данные в выпадающем списке внешнего ключа."""
        if db_field.name == "people":
            kwargs["queryset"] = People.objects.filter(owner_user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
