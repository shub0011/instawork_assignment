FROM python:2
ENV PYTHONUNBUFFERED 1
WORKDIR /assignment
ADD req.txt /assignment/
RUN pip install --upgrade pip
RUN pip install -r req.txt
ADD . /backend/

COPY migrate.sh . 

RUN chmod +x migrate.sh


ENTRYPOINT [ "/bin/bash","migrate.sh"]

EXPOSE 8000