import django_filters
from tracker.models import Tracker


class TrackerFilter(django_filters.FilterSet):
    """Фильтры для модели TACKER """

    # Фильтрует по статусу tracker
    status = django_filters.CharFilter(field_name="status", lookup_expr="exact")

    # Фильтрует по наличию связанных задач
    related_tracker_isnull = django_filters.BooleanFilter(field_name="related_tracker", lookup_expr="isnull")

    # Фильтрует по статусу связанной задачи
    related_tracker_status = django_filters.CharFilter(field_name="related_tracker__status", lookup_expr="exact")

    class Meta:
        model = Tracker
        fields = ['status', 'related_tracker_isnull', 'related_tracker_status']
