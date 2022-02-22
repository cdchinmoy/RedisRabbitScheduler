import pika
import time
import notify
import os
import json
import logging

url = os.environ['CLOUDAMQP_URL']
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) 

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Waiting for messages.')


def callback(ch, method, properties, body):
    data = json.loads(body)
    notify.send_mail(data)
    print(" [x] Done")
    logging.info('Sending notification mail...')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()