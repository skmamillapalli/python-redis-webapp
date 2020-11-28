FROM python:latest
EXPOSE 5000
ADD app.py app.py
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD [ "python3", "app.py" ]
