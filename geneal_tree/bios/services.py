from core.service import BaseService
from bios.models import BioPeople
from django.utils.html import format_html


class ServiceBiography(BaseService):
    """Отдельный сервис для работы с биографиями."""

    @staticmethod
    def form_data() -> list[dict]:
        """Сервис для формирования данных в биографию."""
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

        return bios_peoples_end_text
