from rest_framework import serializers
from .models import Mensaje
from polls import views
class MensajeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Mensaje
            fields = '__all__'
            field = ('id', 'mensaje','fecha')


        def create(self, validated_data):
            list = Mensaje.objects.using('default')
            if len(list)-1 > 0:
                ms = list[len(list)-1]
                views.todos(ms,'http://167.99.147.146:8000/archivo/')
            return Mensaje.objects.using('default').create(**validated_data)
