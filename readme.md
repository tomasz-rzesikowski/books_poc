## Books_poc

How to run it:

Create a folder env in main app directory. Add .env file to the folder with content:

DEBUG=1\
SECRET_KEY=django_likes_mango\
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]\
SQL_ENGINE=django.db.backends.postgresql\
SQL_DATABASE=example_django_dev\
SQL_USER=example_django\
SQL_PASSWORD=example_django\
SQL_HOST=db\
SQL_PORT=5432

Add db.env file to env directory with content:

POSTGRES_USER=example_django\
POSTGRES_PASSWORD=example_django\
POSTGRES_DB=example_django_dev

TO START, RUN IN TERMINAL:
1. `docker-compose -f docker-compose.dev.yml up --build`
3. Make separate migration for each application.(should be all done during build) 

`docker-compose exec backend python manage.py makemigrations <application name>`

`docker-compose exec backend python manage.py migrate <application name>` 

4. Check your app at: http://0.0.0.0:8000/
5. To run tests `docker-compose exec backend python manage.py test`
5. Kill it after usage `docker-compose down -v`