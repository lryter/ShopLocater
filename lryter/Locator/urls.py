from django.conf.urls import include, url,  patterns
from django.contrib import admin
from rest_framework import routers,  serializers,  viewsets
from ShopLocater.views import TaskViewSet,  UserViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'task',  TaskViewSet)
router.register(r'user',  UserViewSet)

urlpatterns = [
    url(r'^',  include('ShopLocater.urls')), 
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns = patterns('', 
(r'^',  include('ShopLocater.urls')), 
(r'^json/',  include(router.urls)), 
(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
