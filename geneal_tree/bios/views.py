from django.views.generic import View
from django.template.response import TemplateResponse
from bios.services import ServiceBiography


class BioPeopleView(View):
    """Вью, который возвращает биографии."""

    def get(self, request):
        """Получает основную страницу c биографиями."""
        bios_peoples_end_text = ServiceBiography.form_data()
        return TemplateResponse(
            request,
            template='search_bio.html',
            context={
                'message_for_user': 'Нажмите на имя чтобы узнать биографию человека',
                'bios_people':  bios_peoples_end_text
            }
        )

