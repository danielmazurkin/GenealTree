import functools
from users.models import AllowedUser
from django.db.models import Q


def check_right_access(func):
    """Проверка прав на доступ к данному эндпоинту"""
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):

        try:
            request = args[0]
            is_allow_bio = AllowedUser.objects.filter(
                Q(user_linked__pk=request.user.pk) |
                Q(owner_user=request.user)
            ).exists()
            kwargs['has_access'] = is_allow_bio
        except (TypeError, IndexError):
            kwargs['has_access'] = False

        return func(self, *args, **kwargs)

    return wrap
