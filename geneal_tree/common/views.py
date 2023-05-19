from django.views.generic import View
from django.template.response import TemplateResponse


class CommonView(View):
    """Вью, который возвращает главную страницу."""

    def get(self, request) -> TemplateResponse:
        """Получает основную страницу."""
        return TemplateResponse(
            request,
            template='common.html',
            context={
                'message_for_user': 'Привет, это генеалогическое дерево'
            }
        )
