web: gunicorn todos.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate