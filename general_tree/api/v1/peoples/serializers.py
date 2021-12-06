from rest_framework import serializers
from peoples.models import BioPeople


class BioPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioPeople
        fields = '__all__'

