FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=random_number_consumer.py
CMD ["python", "random_number_consumer.py"]
