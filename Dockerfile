FROM python:3.9

USER root

RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install matplotlib

WORKDIR /app
COPY app /app
COPY start.sh /

RUN chmod 755 /start.sh

CMD ["/start.sh"]