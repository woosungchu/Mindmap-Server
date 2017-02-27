#NCLB - MindMap

##Build
    cd mindmap
    python manage.py runserver


##Technology
Backend
- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](http://www.django-rest-framework.org/)
- [django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt)
- [dj-database-url](https://github.com/kennethreitz/dj-database-url)


Frontend
- [Ember](http://emberjs.com/)
- [Ember-Django-Adapter](http://dustinfarris.com/ember-django-adapter/)
- [Ember simple auth](https://github.com/simplabs/ember-simple-auth)
- [Ember simplet auth token](https://github.com/jpadilla/ember-simple-auth-token)
- [Ember-bootstrap](http://kaliber5.github.io/ember-bootstrap/)

Others
- [Heroku](https://www.heroku.com/)
- [PostgreSql](https://data.heroku.com/)

##TEST
###### Browsable API suffix
- http://127.0.0.1:8000/api/maps.api
- http://127.0.0.1:8000/api/users.api

###### HTTPIE
- http http://127.0.0.1:8000/api/maps Accept:application/json
- http http://127.0.0.1:8000/api/maps.json
- http -a test:test POST http://127.0.0.1:8000/api/maps 
- http POST http://127.0.0.1:8000/api-token-auth/ username=test password=test
