FROM continuumio/miniconda3
RUN conda create -n env python=3.6
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -U pip \
   && pip install -U -r /tmp/requirements.txt
WORKDIR /app
COPY ./src /app
EXPOSE 8050
ARG DB_HOST
ARG DB_USER
ARG DB_PASSWORD
ARG DB_NAME
ARG DB_PORT
ARG MAPBOX_ACCESS_TOKEN
ENV DB_HOST=$DB_HOST
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_NAME=$DB_NAME
ENV DB_PORT=$DB_PORT
ENV MAPBOX_ACCESS_TOKEN=$MAPBOX_ACCESS_TOKEN
ENTRYPOINT ["python3"]
CMD ["app.py"]
