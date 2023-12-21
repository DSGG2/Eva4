from rest_framework import routers
from .api import ApiViewSet

router=routers.DefaultRouter()

router.register('api/Api',ApiViewSet,'api')

urlpatterns=router.urls
