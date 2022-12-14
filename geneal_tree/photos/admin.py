from photos.models import PhotoPeople
from django.contrib import admin
from photos.forms import ImageUploaderWidgetForm
from photos.models import AvatarPeople


@admin.register(PhotoPeople)
class PhotoPeopleAdmin(admin.ModelAdmin):
    search_fields = ('people__first_name', 'people__last_name', 'people__surname', )
    list_display = ('people', 'photo_link', )
    fields = ('people', 'photo_link', 'description', )
    form = ImageUploaderWidgetForm


@admin.register(AvatarPeople)
class AvatarPeopleAdmin(admin.ModelAdmin):
    search_fields = ('people__name', )
    list_display = ('people', 'photo_link',)
    fields = ('people', 'photo_link', )
    form = ImageUploaderWidgetForm

