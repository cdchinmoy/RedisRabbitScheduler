import pika
import os
import json

def publish(data):
    try:
        url = os.environ['CLOUDAMQP_URL']
        params = pika.URLParameters(url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params) 

        channel = connection.channel()
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=json.dumps(data),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))

        connection.close()
        
    except Exception as e:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")