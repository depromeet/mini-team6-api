from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404

from .serializers import PartySerializer, PartyCreateSerializer
from apps.partys.models import Party


class PartyViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Party.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(
            Q(owner=user) |
            Q(member__in=[user])
        )
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return PartyCreateSerializer
        return PartySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GetParty(APIView):

    def get_object(self, pk):
        try:
            return Party.objects.get(pk=pk)
        except Party.DoesNotExist:
            raise Http404
