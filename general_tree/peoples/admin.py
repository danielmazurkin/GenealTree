from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin
from .models import People
from .models import PhotoPeople
from .models import BioPeople


class PhotoInline(admin.StackedInline):
    model = PhotoPeople
    extra = 1


@admin.register(People)
class AdminPeople(MPTTModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'sex', )
    inlines = [PhotoInline, ]


@admin.register(BioPeople)
class AdminBioPeople(admin.ModelAdmin):
    list_display = ('people', 'text_bio')


@admin.register(PhotoPeople)
class AdminPhotoPeople(admin.ModelAdmin):
    list_display = ('people', 'photo_link')
    fields = ('people', 'image_tag', )
    readonly_fields = ('people', 'image_tag',)

    def image_tag(self, obj):
        """Возвращаем картинку человека в админке."""
        return mark_safe('<img src="{url}" width="200px" height="200px" />'.format(
            url=obj.photo_link.url,
            width=obj.photo_link.width,
            height=obj.photo_link.height,
        ))

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True
