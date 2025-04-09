FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8001

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "psf.wsgi:application"]
