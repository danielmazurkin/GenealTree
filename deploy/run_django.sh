#!/bin/sh

python "manage.py" collectstatic --noinput

python "manage.py" migrate --noinput

gunicorn -c "gunicorn.conf.py" general_tree.wsgi:application
