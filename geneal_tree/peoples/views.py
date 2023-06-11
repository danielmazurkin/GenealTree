import json
from django.views import View
from django.template.response import TemplateResponse
from peoples.services import TreeService
from common.right_access_decorator import check_right_access


class TreeView(View):

    @check_right_access
    def get(self, request, pk, *args, **kwargs):
        context_data = {}

        if kwargs['has_access'] or int(pk) == request.user.pk:
            result_dict_tree = TreeService.form_data(pk_user=pk)
            context_data['result_dict_tree'] = json.dumps(result_dict_tree)
        else:
            context_data['error_access'] = True

        return TemplateResponse(
            request,
            template='tree_template.html',
            context=context_data
        )
