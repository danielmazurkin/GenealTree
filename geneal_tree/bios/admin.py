from django.contrib import admin
from bios.models import BioPeople
from common.people_admin_mixin import PeopleAdminMixin


@admin.register(BioPeople)
class AdminBioPeople(PeopleAdminMixin, admin.ModelAdmin):
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
