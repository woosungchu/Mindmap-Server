from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns=[
    url(r'^api-token-auth/', obtain_jwt_token, name="login"),
    url(r'^api-token-refresh/', refresh_jwt_token, name="jwt-refresh"),
]
