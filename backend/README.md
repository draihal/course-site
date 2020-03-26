# Django Courses Site (Backend part)
> This is a courses site on Django built for learning.


## About
This is a courses site on Django.

API specification:
- A swagger-ui view at api/v1/
- A JSON view at api/v1/swagger.json
- A YAML view at api/v1/swagger.yaml
- A ReDoc view at api/v1/redoc/


## Dependencies
The base project dependencies:

- python version 3.6 +
- django 2.2
- PostgreSQL 
- djangorestframework 3.10
- celery  with extras "redis" 4.3
- redis 3.3

The complete list of dependencies can be found at Pipfile.

## Tests
Run in cli:
```python
pytest
```

