from django.forms import DateInput
from rest_framework import serializers

from .models import Master

class MasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = ('id', 'industry', 'oppNumber', 'name', 'prodCode', 'request', 'sales', 'projManager', 'engineer', 'reqDate', 'dueDate', 'compDate', 'comments' )
        widgets = {
            'reqDate': DateInput(),
            'dueDate': DateInput(),
            'compDate': DateInput()
        }