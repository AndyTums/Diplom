from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from tracker.filters import TrackerFilter
from tracker.models import Tracker
from tracker.serializer import TrackerSerializer


class TrackerViewset(viewsets.ModelViewSet):
    """ViewSet для модели TACKER"""

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TrackerFilter
    ordering_fields = ('id', 'status')
