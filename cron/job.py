from curses import flash
from rpc_publisher import RpcClient
from notification_publisher import publish
import json
import redis
from datetime import datetime

redis_client = redis.Redis(host='redis', port=6379)

def first_job():
    data = {'target_function':'assigned_zero'}
    rpcclient = RpcClient()
    response = rpcclient.call(json.dumps(data))
    job_count = response.decode('utf-8')

    if int(job_count) > 0:
        subject = "First Mail"
        mail_body = str(job_count)+" numbers of tasks are available."
        receiver_list = "cdchinmoy@gmail.com","express.chinmoy@gmail.com"
        data = {'subject':subject, 'mail_body':mail_body, 'receiver_list':receiver_list}
        publish(data)

def second_job():
    data = {'target_function':'assigned_one'}
    rpcclient = RpcClient()
    response = rpcclient.call(json.dumps(data))
    job_count = response.decode('utf-8')

    if int(job_count) > 0:
        subject = "Second Mail"
        mail_body = "No task available!"
        receiver_list = "cdchinmoy@gmail.com","express.chinmoy@gmail.com"
        data = {'subject':subject, 'mail_body':mail_body,'receiver_list':receiver_list}
        publish(data)
