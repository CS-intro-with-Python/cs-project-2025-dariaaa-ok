#FROM python:3.11
#
#WORKDIR /app
#
#COPY . /app
#
#RUN pip install -r requirements.txt
#
#CMD ["python","server.py"]

FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

CMD ["flask", "run"]



#ENV FLASK_APP=server.py
#ENV FLASK_RUN_RELOAD=true
#CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
##ENTRYPOINT ["python","server.py"]
