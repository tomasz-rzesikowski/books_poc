## Books_poc

How to run it:

Create a file .env in main app directory with content:

```properties
DEBUG=1
SECRET_KEY=django_likes_mango
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=book_poc
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=book_poc
```


TO START, RUN IN TERMINAL:
1. `docker-compose up --build`
2. Check your app at: http://127.0.0.1:8000/
3. To run tests `docker-compose exec backend python manage.py test`
4. Kill it after usage `docker-compose down -v`