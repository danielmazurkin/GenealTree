from django.views import View
from django.template.response import TemplateResponse
from .models import People


class TreeView(View):
    greeting = "Good Day"

    def get(self, request):

        nodes = People.objects.all()

        return TemplateResponse(
            request,
            template='tree_template.html',
            context={
                'nodes': nodes
            }
        )
