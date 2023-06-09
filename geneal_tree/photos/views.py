from django.views import View
from django.template.response import TemplateResponse
from photos.services import PhotoService
from users.models import AllowedUser
from django.db.models import Q


class PhotoView(View):
    """Вью, который возвращает главную страницу."""

    def get(self, request, pk):
        """Получает фотографии пользователя."""
        context_data = {}

        is_allow_photo = AllowedUser.objects.filter(
            Q(user_linked__pk=request.user.pk) |
            Q(owner_user=request.user)
        ).exists()

        if is_allow_photo or int(pk) == request.user.pk:
            urls_images = PhotoService.form_data(pk_user=int(pk))
            context_data['images'] = urls_images
        else:
            context_data['error_access'] = True

        return TemplateResponse(
            request,
            template='photos.html',
            context=context_data
        )
