import redis
import random
import time
import threading

def subscribe():
    conn = redis.Redis()

    topic = 'topic_1'

    sub = conn.pubsub()
    sub.subscribe([topic])
    cnt = 0
    for msg in sub.listen():
        if msg['type'] == 'message':
            msg_channel = msg['channel']
            msg_data = msg['data']
            print('{}\'s message: {}'.format(msg_channel, msg_data))
            if(msg_data == 'end'):
                break