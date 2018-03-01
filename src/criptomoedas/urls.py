from django.urls import path, include
from rest_framework import routers

from .views import MoedaModelViewSet

router = routers.SimpleRouter()
router.register(r'moedas', MoedaModelViewSet, base_name="moedas")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
