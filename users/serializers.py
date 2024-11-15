
from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "user",
            "payment_date",
            "paid_course",
            "separately_paid_lesson",
            "payment_amount",
            "payment_method",
        ]


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'phone', 'city')



