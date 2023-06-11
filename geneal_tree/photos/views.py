from django.views import View
from django.template.response import TemplateResponse
from photos.services import PhotoService
from common.right_access_decorator import check_right_access


class PhotoView(View):
    """Вью, который возвращает главную страницу."""

    @check_right_access
    def get(self, request, pk, *args, **kwargs):
        """Получает фотографии пользователя."""
        context_data = {}

        if kwargs['has_access'] or int(pk) == request.user.pk:
            urls_images = PhotoService.form_data(pk_user=int(pk))
            context_data['images'] = urls_images
        else:
            context_data['error_access'] = True

        return TemplateResponse(
            request,
            template='photos.html',
            context=context_data
        )
