from rest_framework import serializers

from hrm.models import Users

class UserSerializer(serializers.ModelSerializer):
    emp_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

    class Meta:
        model = Users
        fields  = '__all__'

