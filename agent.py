import grpc
import os

import master_pb2
import master_pb2_grpc

## python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. master.proto
def run():
    master_ip = os.getenv('MASTER_SERVICE_HOST', 'localhost')
    master_port = '50051'
    with grpc.insecure_channel(f'{master_ip}:{master_port}') as channel:
        stub = master_pb2_grpc.MasterServiceStub(channel)
        response = stub.GetResponse(master_pb2.MasterRequest(message='Hello from Agent'))
        print("Master responded with: " + response.message)

if __name__ == '__main__':
    run()
