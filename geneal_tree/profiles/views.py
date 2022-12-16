from django.views.generic.base import TemplateView

from peoples.models import People
from profiles.services import ProfileService


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        people = People.objects.filter(
            pk=kwargs["id"]
        ).first()

        ProfileService.form_data_for_context(context, people)

        return context
