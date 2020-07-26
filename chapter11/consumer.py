def consumer(consumeQ):
    sentinel = -1
    # 데이터를 2배
    while True:
        data = consumeQ.get()
        print('data found to be processed: {}'.format(data), '\n')
        processed = data * 2
        print('processed: {}'.format(processed), '\n')
        if data is sentinel:
            break