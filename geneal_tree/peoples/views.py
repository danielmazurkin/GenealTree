import json
from django.views import View
from django.template.response import TemplateResponse
from peoples.services import TreeService
from users.models import AllowedUser
from django.db.models import Q
from peoples.models import People


class TreeView(View):
    def get(self, request, pk):
        context_data = {}

        is_allow_tree = AllowedUser.objects.filter(
            Q(user_linked__pk=request.user.pk) |
            Q(owner_user=request.user)
        ).exists()

        if is_allow_tree or int(pk) == request.user.pk:
            result_dict_tree = TreeService.form_data(pk_user=pk)
            context_data['result_dict_tree'] = json.dumps(result_dict_tree)
        else:
            context_data['error_access'] = True

        return TemplateResponse(
            request,
            template='tree_template.html',
            context=context_data
        )
