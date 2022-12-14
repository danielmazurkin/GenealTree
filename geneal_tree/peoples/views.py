import json
from django.views import View
from django.template.response import TemplateResponse
from peoples.services import TreeService


class TreeView(View):
    greeting = "Good Day"

    def get(self, request):
        result_dict_tree = TreeService.build_tree()
        return TemplateResponse(
            request,
            template='tree_template.html',
            context={
                'result_dict_tree': json.dumps(result_dict_tree)
            }
        )
