FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/LandAccounting

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements.txt
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999 postgres


COPY . /usr/src/LandAccounting

EXPOSE 8000



#FROM postgres:12-bullseye
#
#LABEL maintainer="PostGIS Project - https://postgis.net"
#
#ENV POSTGIS_MAJOR 3
#ENV POSTGIS_VERSION 3.3.2+dfsg-1.pgdg110+1
#
#RUN apt-get update \
#      && apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
#      && apt-get install -y --no-install-recommends \
#           # ca-certificates: for accessing remote raster files;
#           #   fix: https://github.com/postgis/docker-postgis/issues/307
#           ca-certificates \
#           \
#           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
#           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts \
#      && rm -rf /var/lib/apt/lists/*
#
#RUN mkdir -p /docker-entrypoint-initdb.d
#COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/10_postgis.sh
#COPY ./update-postgis.sh /usr/local/bin