from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from employee.models import Employee
from tracker.filters import TrackerFilter
from tracker.models import Tracker
from tracker.serializer import TrackerSerializer


class TrackerViewset(viewsets.ModelViewSet):
    """ViewSet для модели TRACKER"""

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TrackerFilter
    ordering_fields = ('id', 'status')

    def list(self, request, *args, **kwargs):
        """Вывод информации списка согласно шаблона"""

        filter_params = request.query_params
        print(filter_params)

        # Проверяем наличие фильтра в запросе
        if filter_params is not None and filter_params.get("important_trackers") is True:

            # Формируем ответ, если есть отфильтрованные задачи
            queryset = self.filter_queryset(self.get_queryset())  # Получаем отфильтрованный queryset
            serializer = self.get_serializer(queryset, many=True)  # Сериалзация
            formatted_response = []

            for item in serializer.data:
                # Получаем ID сотрудников
                employee_ids = item['employees']
                # Фильтруем сотрудник по ID
                employee_info = Employee.objects.filter(id__in=employee_ids)

                # Достаем ФИО каждого необходимого сотрудника
                employee_names = [employee.fio for employee in employee_info]

                # Создаем необходимый формат ответа
                formatted_response.append({

                    "Важная задача": item['title'],
                    "Срок выполнения": item['time'],
                    "Выполняющие": employee_names,
                })

            return Response(formatted_response)

        else:
            queryset = self.filter_queryset(self.get_queryset())  # Получаем все объекты
            serializer = self.get_serializer(queryset, many=True)  # Сериализация
            return Response(serializer.data)
