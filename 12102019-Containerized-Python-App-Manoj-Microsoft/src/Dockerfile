FROM python:alpine3.7
ENV FLASK_PORT=5003
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["python"]
CMD ["app.py"]