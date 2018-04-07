from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.partys.models import Party

from  .serializers import PartySerailzier


class PartyViewSet(ModelViewSet):

    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = PartySerailzier
    queryset = Party.objects.all()

class GetParty()