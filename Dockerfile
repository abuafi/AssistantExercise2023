FROM python:3

ADD . /

RUN pip3 install bs4 requests

RUN ["python3", "src/test.py"]

ENTRYPOINT ["python3", "src/main.py"]