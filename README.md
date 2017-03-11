#MindMap-Server

- Mindmap-App : [Application](https://github.com/woosungchu/Mindmap-App)
- Mindmap-Web : [Frontend](https://github.com/woosungchu/Mindmap-Web)


##Technology

- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](http://www.django-rest-framework.org/)
- [django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt)
- [dj-database-url](https://github.com/kennethreitz/dj-database-url)

##TEST
##### Browsable API suffix
- http://127.0.0.1:8000/api/maps.api
- http://127.0.0.1:8000/api/users.api

##### HTTPIE
- http http://127.0.0.1:8000/api/maps Accept:application/json
- http http://127.0.0.1:8000/api/maps.json
- http -a test:test POST http://127.0.0.1:8000/api/maps
- http POST http://127.0.0.1:8000/api-token-auth/ username=test password=test

#### Refrences
- [Status Code](http://www.django-rest-framework.org/api-guide/status-codes/)
- [REST api pattern](http://www.django-rest-framework.org/api-guide/routers/#defaultrouter)
