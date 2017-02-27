from django.conf.urls import url, include
from users import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns=[
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]
