celery -A storefront worker --loglevel=info

python manage.py runserver


Im suppose to run code and go to(http://127.0.0.1:8000/playground/hello/)using celery and the back end should return some tasks to me but it isnt workin 

related codes are in the storefront/celery & playground/tasks