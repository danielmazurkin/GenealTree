from django.views import View
from django.template.response import TemplateResponse
from photos.services import PhotoService


class PhotoView(View):
    """Вью, который возвращает главную страницу."""

    def get(self, request):
        """Получает фотографии пользователя."""
        urls_images = PhotoService.form_data()

        return TemplateResponse(
            request,
            template='photos.html',
            context={
                'images': urls_images
            }
        )
