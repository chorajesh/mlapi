FROM python:3.8

RUN rm -rf /app
RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN pip list
ENTRYPOINT ["python"]
CMD ["run.py"]