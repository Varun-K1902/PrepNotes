release: python manage.py makemigrations && python manage.py migrate && python manage.py tailwind init && python manage.py tailwind install
web: gunicorn PrepNotes.wsgi