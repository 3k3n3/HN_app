from rest_framework import serializers
from app.models import Base

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['by', 'title', 'post_type', 'text', 'time', 'url']