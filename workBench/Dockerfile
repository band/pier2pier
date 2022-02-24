FROM python:3.10.2-slim-buster
WORKDIR /usr/src/app
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
#Server reloads itself on file changes if in dev mode
ENV FLASK_ENV=development 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
