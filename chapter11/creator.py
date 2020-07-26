def creator(createQ, consumeQ):
    # 데이터를 생성하고 consumeQ 에 넘겨줌
    sentinel = -1
    while True:
        data = createQ.get()
        print('data found to be consumed: {} \n'.format(data))
        
        if(type(data) == str):
            consumeQ.put(data)
            raise ValueError()
        
        consumeQ.put(data)
        if data is sentinel:
            break