from concurrent import futures
import grpc
import time

import master_pb2
import master_pb2_grpc

## python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. master.proto 
class MasterService(master_pb2_grpc.MasterServiceServicer):
    def GetResponse(self, request, context):
        return master_pb2.MasterResponse(message='Hello from Master')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterServiceServicer_to_server(MasterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
