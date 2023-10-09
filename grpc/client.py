import math_pb2_grpc, math_pb2
import grpc

channel = grpc.insecure_channel("localhost:5440")

# When we call functions on CalcStub, all the networking backend is handled for us (send to server and return response)
stub = math_pb2_grpc.CalcStub(channel)  # format: <PROTONAME>_pb2_grpc.<STUBFROM pb2_grpc.py>Stub

# so this won't run on the client, but on the server:
resp = stub.Mult(math_pb2.MultReq(x=3, y=4))
print(resp)

resp = stub.MultMany(math_pb2.MultManyReq(nums=[2, 3, 4]))
print(resp)
