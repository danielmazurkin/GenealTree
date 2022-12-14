from django.views.generic.base import TemplateView

from peoples.models import People
from django.conf import settings
from django.utils.html import mark_safe


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        people = People.objects.filter(
            pk=kwargs["id"]
        ).first()

        context['photos'] = []
        context['avatar'] = getattr(people, 'avatarpeople', None)
        context['name_people'] = str(people)

        if context['avatar']:
            context['avatar'] = f"{settings.SITE_URL}{context['avatar'].photo_link.url}"

        if people:
            photos = people.photopeople_set.all()

            for photo in photos:
                context['photos'].append(
                    f'{settings.SITE_URL}{str(photo.photo_link.url)}'
                )

        if hasattr(people, 'biopeople'):
            context['biopeople'] = mark_safe(people.biopeople)

        return context
