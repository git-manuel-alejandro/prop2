from dataclasses import field
from rest_framework import serializers
from publicacion.models import Publicacion


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id', 'title', 'description', 'direccion', 'price',
                  'business', 'published', 'created_at', 'updated_at']
