FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY agent.py agent.py
COPY master.proto master.proto
COPY master_pb2.py master_pb2.py
COPY master_pb2_grpc.py master_pb2_grpc.py

CMD ["python", "agent.py"]
