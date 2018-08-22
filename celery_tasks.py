from celery import Celery
from kombu import Exchange, Queue
from celery.exceptions import Reject
import requests
import os


default_queue_name = 'default'
default_exchange_name = 'default'
default_routing_key = 'default'

sunshine_queue_name = 'sunshine'
sunshine_routing_key = 'sunshine'

moon_queue_name = 'moon'
moon_routing_key = 'moon'

app = Celery(
    'tasks',
    backend='rpc://', broker='amqp://localhost//')

default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key)

sunshine_queue = Queue(
    sunshine_queue_name,
    default_exchange,
    routing_key=sunshine_routing_key)

moon_queue = Queue(
    moon_queue_name,
    default_exchange,
    routing_key=moon_queue_name)

app.conf.task_queues = (default_queue, sunshine_queue, moon_queue)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key


@app.task
def add(x, y):
    import time
    time.sleep(30)
    while True:
        print "*****************8"
    return x + y


@app.task
def download(url, filename):
    """
    Download a page and save it to the BASEDIR directory
      url: the url to download
      filename: the filename used to save the url in BASEDIR
    """
    response = requests.get(url)
    data = response.text
    with open(filename, 'wb') as file:
        file.write("****************")
    file.close()