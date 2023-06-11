from photos.models import PhotoPeople
from django.contrib import admin
from photos.forms import ImageUploaderWidgetForm
from photos.models import AvatarPeople
from common.people_admin_mixin import PeopleAdminMixin


@admin.register(PhotoPeople)
class PhotoPeopleAdmin(PeopleAdminMixin, admin.ModelAdmin):
    search_fields = ('people__first_name', 'people__last_name', 'people__surname', )
    list_display = ('people', 'photo_link', )
    fields = ('people', 'photo_link', 'description', )
    form = ImageUploaderWidgetForm

    def save_model(self, request, obj, form, change):
        """Переопределение сохранения модели для создания многопользовательского режима."""
        obj.owner_user = request.user
        obj.save()

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)



@admin.register(AvatarPeople)
class AvatarPeopleAdmin(PeopleAdminMixin, admin.ModelAdmin):
    search_fields = ('people__name', )
    list_display = ('people', 'photo_link',)
    fields = ('people', 'photo_link', )
    form = ImageUploaderWidgetForm

    def save_model(self, request, obj, form, change):
        """Переопределение сохранения модели для создания многопользовательского режима."""
        obj.owner_user = request.user
        obj.save()

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)

