from rest_framework.viewsets import ModelViewSet
from publicacion.api.serializers import PublicacionSerializer
from publicacion.models import Publicacion


class PublicacionView(ModelViewSet):
    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()
