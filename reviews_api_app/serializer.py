from rest_framework import serializers
from .models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'item', 'review', 'purchaser')
        model = Reviews