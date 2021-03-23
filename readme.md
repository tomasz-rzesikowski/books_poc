## Books_poc

How to run it:

1. Rename a file .env-default to .env in main app directory.
2. To start, run in terminal `docker-compose up --build`
3. At this point, your Django app should be running at port 8000 on your Docker host.
   On Docker Desktop for Mac and Docker Desktop for Windows,
   go to http://localhost:8000 on a web browser to see the Django welcome page.
4. To run tests, run in terminal `docker-compose exec backend python manage.py test`
5. Kill it after usage, run in terminal `docker-compose down -v`
