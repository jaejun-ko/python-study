def creator(create_queue, consume_queue):
    # 들어온 데이터 출력
    sentinel = -1
    while True:
        data = create_queue.get()
        print('data found to be consumed: {} \n'.format(data))
        
        consume_queue.put(data)
        
        if data is sentinel:
            create_queue.task_done()
            create_queue.join()
            break