import pika, os
import function
import json

url = os.environ['CLOUDAMQP_URL']
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) 

channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def action(data):

    data = json.loads(data)
    function_name = data['target_function']
    if function_name == 'assigned_zero':
        res = function.assigned_zero()
        return res
    elif function_name == 'assigned_one':
        res = function.assigned_one()
        return res
    else:
        pass   

def on_request(ch, method, props, body):
    data = body
    response = action(data)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()