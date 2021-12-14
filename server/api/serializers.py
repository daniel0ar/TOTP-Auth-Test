from rest_framework import serializers

from .models import TOTP, TOTPLog


class TOTPSerializer(serializers.ModelSerializer):
    secret = serializers.CharField(max_length=20)
    userId = serializers.IntegerField()

    def create(self, validated_data):
        return TOTP.objects.create(
            secret=validated_data.get('secret'),
            userId=validated_data.get('userId')
        )

    class Meta:
        model = TOTP
        fields = (
            'secret',
            'userId'
        )

class TOTPLogSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    token = serializers.CharField(max_length=6)
    userId = serializers.IntegerField()

    def create(self, validated_data):
        return TOTPLog.objects.create(
            date=validated_data.get('date'),
            token=validated_data.get('token'),
            userId=validated_data.get('userId')
        )

    class Meta:
        model = TOTPLog
        fields = (
            'date',
            'token',
            'userId'
        )