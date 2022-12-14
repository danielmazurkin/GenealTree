from django.views import View
from photos.models import PhotoPeople
from django.template.response import TemplateResponse
from django.core.paginator import Paginator


class PhotoView(View):
    """Вью, который возвращает главную страницу."""

    def get(self, request):
        """Получает основную страницу."""
        photos = PhotoPeople.objects.all()

        urls_images = []
        for photo in photos:
            urls_images.append(photo)

        return TemplateResponse(
            request,
            template='photos.html',
            context={
                'images': urls_images
            }
        )
