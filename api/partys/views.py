from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.partys.models import Party

from  .serializers import PartySerailzier

class PartyView(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = PartySerailzier
    queryset = Party.objects.all()

