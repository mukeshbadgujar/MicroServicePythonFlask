import pika
import json
import time


def callback(ch, method, properties, body):
	message = json.loads(body)
	print(f"Received message: {message}")


def start_consumer():
	try:
		# Use 'rabbitmq' as the hostname
		# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
		connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
		channel = connection.channel()
		
		# Declare the queue
		channel.queue_declare(queue='random_number_queue')
		
		# Set up subscription on the queue
		channel.basic_consume(queue='random_number_queue', on_message_callback=callback, auto_ack=True)
		
		print('Waiting for messages. To exit, press CTRL+C')
		channel.start_consuming()
	except pika.exceptions.AMQPConnectionError as err:
		print("Waiting for RabbitMQ to be available...", err)
		time.sleep(5)  # Wait for 5 seconds before retrying


if __name__ == '__main__':
	start_consumer()
