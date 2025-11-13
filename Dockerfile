FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python","server.py"]

#ENV FLASK_APP=server.py
#ENV FLASK_RUN_RELOAD=true
#CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
##ENTRYPOINT ["python","server.py"]
