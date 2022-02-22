import pika,os
import uuid

class RpcClient(object):

    def __init__(self):

        self.url = os.environ['CLOUDAMQP_URL']
        self.params = pika.URLParameters(self.url)
        self.params.socket_timeout = 5

        self.connection = pika.BlockingConnection(self.params) 
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, data):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=data)
        while self.response is None:
            self.connection.process_data_events()
        return self.response