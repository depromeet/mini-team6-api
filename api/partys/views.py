from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.partys.models import Party
from django.http import Http404
from  .serializers import PartySerailzier


class PartyViewSet(ModelViewSet):

    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = PartySerailzier
    queryset = Party.objects.all()


class GetParty(APIView):

    def get_object(self, pk):
        try:
            return Party.objects.get(pk=pk)
        except Party.DoesNotExist:
            raise Http404