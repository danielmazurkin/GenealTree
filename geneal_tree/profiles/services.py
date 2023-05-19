from core.service import BaseService


class ProfileService(BaseService):
    """Сервис для формирования данных профиля."""

    @staticmethod
    def form_data_for_context(context, people) -> dict:
        context['photos'] = people.photos_link
        context['name_people'] = str(people)
        context['avatar'] = people.avatar_url
        context['biopeople'] = people.bio_people
        return context
