from xmlrpc.server import SimpleXMLRPCServer

# 로그파일 남기
def savelog(msg):
    f = open('my_log.log', 'at')
    f.write('\n' + msg)
    f.close()
    return "log complete: {}".format(msg)

def open_rpc_server():
    address = ('localhost', 3333)
    server = SimpleXMLRPCServer(address)
    print('server started')
    server.register_function(savelog,"log")
    server.serve_forever()

