"""
WSGI config for redcross project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
import sys
sys.path.append("/home/grovesr/.virtualenvs/rims-django1.9/local/lib/python2.7/site-packages")
sys.path.append("/home/grovesr/git/redcross-regions/redcross-eny")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redcross_eny.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
