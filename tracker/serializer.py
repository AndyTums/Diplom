from rest_framework import serializers
from tracker.models import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели TRACKER """

    class Meta:
        model = Tracker
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     return {
    #         'Важная задача': representation['title'],
    #         'Срок': representation['time'],
    #         '[ФИО сотрудника]': representation['employee']['fio'],
    #     }
