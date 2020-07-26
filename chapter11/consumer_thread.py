def consumer(consume_queue, num):
    sentinel = -1
    # 데이터를 2배
    while True:
        data = consume_queue.get()
        print('data found to be processed: {} \n'.format(data))
        processed = data * 2
        print('processed by consumer_{}: {} \n'.format(num, processed))
        if data is sentinel:
            consume_queue.task_done()
            consume_queue.join()
            break