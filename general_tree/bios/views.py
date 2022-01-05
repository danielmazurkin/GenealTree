from django.views.generic import View
from django.template.response import TemplateResponse
from peoples.models import BioPeople


class BioPeopleView(View):
    """Вью, который возвращает главную страницу."""

    greeting = 'Common View'

    def get(self, request):
        bios_peoples = BioPeople.objects.select_related(
            'people'
        ).all()

        """Получает основную страницу."""
        return TemplateResponse(
            request,
            template='search_bio.html',
            context={
                'message_for_user': 'Нажмите на имя чтобы узнать его биографию',
                'bios_people':  bios_peoples
            }
        )

