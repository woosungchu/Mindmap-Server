from django.conf.urls import url, include
from maps import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'maps', views.MapViewSet)

urlpatterns=[
    url(r'^api/', include(router.urls, namespace='api-map')),
]
