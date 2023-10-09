FROM ubuntu:23.10
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install grpcio==1.58.0 grpcio-tools==1.58.0 --break-system-packages
COPY math.proto /var/run/math.proto
CMD ["python3", "-m", "grpc_tools.protoc", "-I=/var/run/", "--python_out=/var/run/", "--grpc_python_out=/var/run", "math.proto"]
