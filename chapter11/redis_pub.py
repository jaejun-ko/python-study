import redis
import random
import time

def publish():
    conn = redis.Redis()

    topics = ['topic_1', 'topic_2']
    contents = ['Hello', 'python']

    for num in range(10):
        topic = random.choice(topics)
        content = random.choice(contents)
        print('publish msg \'{}\' to {}'.format(content,topic))
        conn.publish(topic, content)
        time.sleep(1)

    conn.publish(topics[0], 'end')