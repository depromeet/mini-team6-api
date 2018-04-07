from rest_framework import serializers
from apps.partys.models import Party

class PartySerailzier(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = '__all__'