# Dockerfile for Readers application

FROM python:2.7-onbuild

ENV DJANGO_CONFIGURATION Docker

CMD ["gunicorn", "-c", "gunicorn_conf.py", "--chdir", "cms", "cms.wsgi:application", "--reload"]
