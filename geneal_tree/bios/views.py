from django.views.generic import View
from django.template.response import TemplateResponse
from peoples.models import BioPeople
from django.utils.html import format_html


class BioPeopleView(View):
    """Вью, который возвращает главную страницу."""

    greeting = 'Common View'

    def get(self, request):
        """Получает основную страницу c биографиями."""

        bios_peoples = BioPeople.objects.select_related(
            'people',
        ).all()

        bios_peoples_end_text = []

        for bio in bios_peoples:
            bios_peoples_end_text.append(
                {
                    'name': str(bio.people),
                    'text': format_html(bio.text_bio),
                    'pk': bio.pk,
                }
            )

        return TemplateResponse(
            request,
            template='search_bio.html',
            context={
                'message_for_user': 'Нажмите на имя чтобы узнать биографию человека',
                'bios_people':  bios_peoples_end_text
            }
        )

