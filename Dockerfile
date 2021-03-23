FROM python:3.9

ENV APP_CODE=/app
WORKDIR $APP_CODE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system

COPY . .

RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn books_poc.wsgi:application --bind 0.0.0.0:$PORT