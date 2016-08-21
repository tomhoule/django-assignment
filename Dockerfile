FROM python:3.5

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
VOLUME /data
ENV DEBUG no

CMD /usr/local/bin/gunicorn \
    -b 0.0.0.0:8000 \
    assignment_3mw.wsgi
