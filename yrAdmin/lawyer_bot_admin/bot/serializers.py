from rest_framework import serializers
from .models import JuristName,Payment,User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class JuristnameSerializer(serializers.ModelSerializer):

    class Meta:
        model = JuristName
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):

    jurist = JuristnameSerializer()

    class Meta:
        model = Payment
        fields = '__all__'


