from flask import Flask, jsonify
from rpc_publisher import RpcClient
from notification_publisher import publish
import json
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()


@scheduler.scheduled_job('cron', day='*', hour='18', minute='00')
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


@scheduler.scheduled_job('cron', day='*', hour='21', minute='00')
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


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False,
            host='0.0.0.0', port="5000", threaded=True)