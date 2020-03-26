# Courses Site
> This is a fullstack courses site on Django and Next.js(React) built for learning.


## About
This is a courses site on Django and Next.js(React).
For more details look for README files in backend/frontend folder.

API specification:
- A swagger-ui view at api/v1/
- A JSON view at api/v1/swagger.json
- A YAML view at api/v1/swagger.yaml
- A ReDoc view at api/v1/redoc/


## Dependencies
The base project dependencies:

- docker
- python version 3.6 +
- django 2.2
- PostgreSQL 
- djangorestframework 3.10
- celery  with extras "redis" 4.3
- redis 3.3
- node.js
- next ^9.2.1
- react
- redux

The complete list of dependencies can be found at backend/requirements.txt, backend/requirements-dev.txt and frontend/package.json file.


## Usage
Create 3 files in main folder:
.env.dev 
```
DEBUG=1
SECRET_KEY=*YOUR_KEY*
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] web
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_dev
SQL_USER=django
SQL_PASSWORD=django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
REDIS_URL=redis://redis:6379
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_HOST_USER=*YOUR_EMAIL_HOST_USER*
EMAIL_HOST_PASSWORD=*YOUR_EMAIL_HOST_PASSWORD*
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=noreply@webmaster
CORS_ORIGIN_WHITELIST=http://localhost:3000
SENTRY_DSN=*YOUR_SENTRY_DSN*
```
.env.prod
```
DEBUG=0
SECRET_KEY=*YOUR_KEY*
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] web
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_prod
SQL_USER=django
SQL_PASSWORD=django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
REDIS_URL=redis://redis:6379
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_HOST_USER=*YOUR_EMAIL_HOST_USER*
EMAIL_HOST_PASSWORD=*YOUR_EMAIL_HOST_PASSWORD*
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=noreply@webmaster
CORS_ORIGIN_WHITELIST=http://localhost:3000
SENTRY_DSN=*YOUR_SENTRY_DSN*
```
.env.prod.db
```
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_prod
```
Update the file permissions locally:
```
$ chmod +x app/entrypoint.prod.sh
$ chmod +x app/entrypoint.sh
```

and run docker:
---
### Development:
```
# Up
$ docker-compose up -d --build

# Navigate to:
# - frontend main page http://localhost:3000/ 
# - admin http://localhost:8000/courses-admin/
# - api (swagger) http://localhost:8000/api/v1/
# - api (redoc) http://localhost:8000/api/v1/redoc/ 

# Logs
$ docker-compose logs -f

# if you need to do something inside container
$ docker-compose exec <name of container, for example - web or frontend or db> <command, for example - python manage.py ... >
# example
$ docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

# Down
$ docker-compose down -v
```
#### Tests (in development)
```
# backend pytest
$ docker-compose exec web pytest

# frontend jest
$ docker-compose exec frontend npm run test

# frontend cypress
$ docker-compose exec frontend npm run cypress:open
```

---
### Production:
```
# Up
$ docker-compose -f docker-compose.prod.yml up -d --build

# Navigate to:
# - frontend main page http://localhost:1337/ 
# - admin http://localhost:1337/courses-admin/
# - api (swagger) http://localhost:1337/api/v1/
# - api (redoc) http://localhost:1337/api/v1/redoc/ 

# Logs
$ docker-compose -f docker-compose.prod.yml logs -f

# if you need to do something inside container
$ docker-compose -f docker-compose.prod.yml exec <name of container, for example - web or frontend or db> <command, for example - python manage.py ... > 

# Down
$ docker-compose -f docker-compose.prod.yml down -v
```
---