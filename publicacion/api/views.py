from rest_framework.viewsets import ModelViewSet
from publicacion.api.serializers import PublicacionSerializer
from publicacion.models import Publicacion
from publicacion.api.permissions import IsAdminOrReadOnly


class PublicacionView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()
