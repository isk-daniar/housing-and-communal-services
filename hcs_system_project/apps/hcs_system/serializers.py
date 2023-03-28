from rest_framework import serializers
from .models import PersonalAccount

class PersonalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalAccount
        fields = ('pa', 'name', 'organization', 'address', 'last_payment', 'balance',)