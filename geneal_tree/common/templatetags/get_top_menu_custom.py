from django import template
from django.contrib.auth.models import AbstractUser
from typing import Dict, List
from jazzmin.utils import make_menu
from jazzmin.settings import get_settings


register = template.Library()


@register.simple_tag
def get_top_menu_custom(user: AbstractUser, admin_site: str = "admin") -> List[Dict]:
    """
    Переопределение тега чтобы добавить id пользователя и проверять возможность его отображения
    для текущего пользователя.
    """
    options = get_settings()

    try:
        result_url = f"/tree/{user.pk}/"
        options['topmenu_links'][0]['url'] = result_url
    except (IndexError, KeyError):
        pass

    return make_menu(user, options.get("topmenu_links", []), options, allow_appmenus=True, admin_site=admin_site)
