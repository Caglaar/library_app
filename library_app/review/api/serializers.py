from review.models import Review
from rest_framework import serializers



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        #fields = '__all__'
        exclude = ['book']
        read_only_fields = ['reviewer']