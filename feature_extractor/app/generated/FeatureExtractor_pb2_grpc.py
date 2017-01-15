import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import FeatureExtractor_pb2 as FeatureExtractor__pb2
import FeatureExtractor_pb2 as FeatureExtractor__pb2


class Feature_ExtractorStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeatures = channel.unary_unary(
        '/sqwak.Feature_Extractor/GetFeatures',
        request_serializer=FeatureExtractor__pb2.HelloRequest.SerializeToString,
        response_deserializer=FeatureExtractor__pb2.HelloReply.FromString,
        )


class Feature_ExtractorServicer(object):
  """The greeting service definition.
  """

  def GetFeatures(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Feature_ExtractorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatures,
          request_deserializer=FeatureExtractor__pb2.HelloRequest.FromString,
          response_serializer=FeatureExtractor__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sqwak.Feature_Extractor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
