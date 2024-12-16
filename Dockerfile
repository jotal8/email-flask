FROM python:latest

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir Flask==2.3.3 Flask-RESTful==0.3.9 Flask-Cors==3.0.10 pyjwt

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "--app", "index", "run", "--host=0.0.0.0"]