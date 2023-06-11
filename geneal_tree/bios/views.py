from django.views.generic import View
from django.template.response import TemplateResponse
from bios.services import ServiceBiography
from common.right_access_decorator import check_right_access


class BioPeopleView(View):
    """Вью, который возвращает биографии."""

    @check_right_access
    def get(self, request, pk, *args, **kwargs):
        """Получает основную страницу c биографиями."""
        context_data = {}

        if kwargs['has_access'] or int(pk) == request.user.pk:
            bios_peoples_end_text = ServiceBiography.form_data(pk_user=int(pk))
            context_data['message_for_user'] = 'Нажмите на имя чтобы узнать биографию человека'
            context_data['bios_people'] = bios_peoples_end_text
        else:
            context_data['error_access'] = True

        return TemplateResponse(
            request,
            template='search_bio.html',
            context=context_data
        )

