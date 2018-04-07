from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.partys.models import Party

from  .serializers import PartySerailzier

class PartyView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PartySerailzier

    def get(self,request):
        serializer = PartySerailzier(Party.objects.all(), many=True)
        return Response(serializer.data)