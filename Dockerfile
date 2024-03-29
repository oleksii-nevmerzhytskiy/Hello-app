FROM python:3.8
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ENV DJANGO_SECRET_KEY secret
COPY . /code/