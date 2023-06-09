from django.views.generic import View
from django.template.response import TemplateResponse
from bios.services import ServiceBiography
from django.db.models import Q
from users.models import AllowedUser


class BioPeopleView(View):
    """Вью, который возвращает биографии."""

    def get(self, request, pk):
        """Получает основную страницу c биографиями."""
        context_data = {}

        is_allow_bio = AllowedUser.objects.filter(
            Q(user_linked__pk=request.user.pk) |
            Q(owner_user=request.user)
        ).exists()

        if is_allow_bio or int(pk) == request.user.pk:
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

