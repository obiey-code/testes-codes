# sites/serializers.py

from rest_framework import serializers
from .models import Site

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('uuid', 'name', 'location', 'is_active', 'created_at')
        read_only_fields = ('uuid', 'created_at')