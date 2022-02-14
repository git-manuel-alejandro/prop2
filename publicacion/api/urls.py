from posixpath import basename
from sys import prefix
from rest_framework.routers import DefaultRouter
from publicacion.api.views import PublicacionView

router_publicacion = DefaultRouter()

router_publicacion.register(
    prefix='publicacion', basename='publicacion', viewset=PublicacionView)
