"""The Python implementation of the GRPC helloworld.Greeter server."""
from concurrent import futures
import time
import grpc
from generated import ModelManager_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Model_Manager(ModelManager_pb2.Model_ManagerServicer):

  def GetFeatures(self, request, context):
    return ModelManager_pb2.FeatureListResponse(message='I am the BEST <b>Madona on the Rocks</b>, %s!' % request.name)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  ModelManager_pb2.add_Model_ManagerServicer_to_server(Model_Manager(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
    serve()