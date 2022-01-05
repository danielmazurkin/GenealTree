from django.views import View

from peoples.models import PhotoPeople
from django.template.response import TemplateResponse
from django.core.paginator import Paginator


class PhotoView(View):
    """Вью, который возвращает главную страницу."""

    greeting = 'Photo View'

    def get(self, request):
        """Получает основную страницу."""
        photos = PhotoPeople.objects.select_related(
            'people'
        ).all()
        paginator = Paginator(photos, 2)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return TemplateResponse(
            request,
            template='photos.html',
            context={
                'message_for_user': 'Фотографии людей в древе',
                'page_obj': page_obj
            }
        )
