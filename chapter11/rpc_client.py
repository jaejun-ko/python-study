import xmlrpc.client
import time

def connect_rpc():
    proxy = xmlrpc.client.ServerProxy("http://localhost:3333/")

    log_text = ['please', 'log', 'this', 'message']
    for text in log_text:
        result = proxy.log(text)
        print(result)
        time.sleep(1)

