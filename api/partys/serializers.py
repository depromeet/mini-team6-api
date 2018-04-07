from rest_framework import serializers
from apps.partys.models import Party

class PartySerailzier(serializers.ModelSerializer):

    class Meat:
        model = Party
        fields = '__all__'