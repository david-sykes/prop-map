FROM python:3.6.6


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 80

EXPOSE 5432

WORKDIR /app/src

ENTRYPOINT ["python"]

CMD ["app.py"]