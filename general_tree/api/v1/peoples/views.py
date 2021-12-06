from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from peoples.models import BioPeople
from api.v1.peoples.serializers import BioPeopleSerializer


class PersonalInfoView(ModelViewSet):
    """View for feedback ."""

    queryset = BioPeople.objects.all()
    serializer_class = BioPeopleSerializer

    @action(methods=['get', ], detail=True)
    def get(self, serializer):
        """Расширим вызов save прокидыванием пользователя."""
        pass