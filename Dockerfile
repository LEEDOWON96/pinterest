FROM python:3.9.0

WORKDIR /home/

RUN echo "_cache check_"

RUN git clone https://github.com/LEEDOWON96/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD [ "bash", "-c", "python manage.py collectstatic --noinput --settings=Pinterest.settings.deploy && python manage.py migrate --settings=Pinterest.settings.deploy && gunicorn Pinterest.wsgi --env DJANGO_SETTINGS_MODULE=Pinterest.settings.deploy --bind 0.0.0.0:8000" ]