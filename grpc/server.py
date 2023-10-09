import math_pb2_grpc, math_pb2  # the auto-created files
import grpc
from concurrent import futures
import traceback
import logging

class MyCalc(math_pb2_grpc.CalcServicer):
    def Mult(self, request, context):
        try:
            print("hi")
            print(request)
            return math_pb2.MultResp(result = request.x * request.y)
        except Exception as e:
            logging.error(traceback.format_exc())
    
    def MultMany(self, request, context):
        try:
            total = 1
            for num in request.nums:
                total *= num
            return math_pb2.MultResp(result = total)
        except Exception as e:
            logging.error(traceback.format_exc())

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[("grpc.so_reuseport", 0)])

# add servicer (using definition from math_pb2_grpc.py)
math_pb2_grpc.add_CalcServicer_to_server(MyCalc(), server) # could use either MyCalc() or math_pb2_grpc.CalcServicer()

server.add_insecure_port('0.0.0.0:5440')
server.start()
print("started")
server.wait_for_termination()

