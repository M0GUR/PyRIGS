#!/bin/bash
cd /var/app
source bin/activate

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
mkdir -p /var/logs/gunicorn
touch /var/logs/gunicorn/gunicorn.log
touch /var/logs/gunicorn/access.log
tail -n 0 -f /var/logs/gunicorn/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn PyRIGS.wsgi:application \
    --name PyRIGS \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/var/logs/gunicorn/gunicorn.log \
    --access-logfile=/var/logs/gunicorn/access.log \
    "$@"
