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
        """ Вывод информации списка согласно шаблона """

        # Получаем отфильтрованные задачи
        filtered_queryset = self.filter_queryset(self.get_queryset())

        if filtered_queryset.exists():

            # Формируем ответ, если есть отфильтрованные задачи
            serializer = self.get_serializer(filtered_queryset, many=True)

            formatted_response = []

            for item in serializer.data:

                # Получаем ID сотрудников и извлекаем их информацию
                employee_ids = item['employees']
                employee_info = Employee.objects.filter(id__in=employee_ids)

                # Форматируем ответ для каждой задачи
                employee_names = [employee.fio for employee in employee_info]  # Достаев ФИО аждого сотрудника

                formatted_response.append({
                    "Важная задача": item['title'],
                    "Срок выполнения": item['time'],
                    "Выполняющие": employee_names,  # Добавляем имена сотрудников
                })

            return Response(formatted_response)  # Возвращаем сформированный ответ после цикла
        else:
            # Если задач нет, возвращаем пустой список
            return Response([])
