# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FeatureExtractor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FeatureExtractor.proto',
  package='sqwak',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x46\x65\x61tureExtractor.proto\x12\x05sqwak\"\x1e\n\x0e\x41udioFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"-\n\x13\x46\x65\x61tureListResponse\x12\x16\n\x0e\x66\x65\x61ture_vector\x18\x04 \x03(\t2Y\n\x11\x46\x65\x61ture_Extractor\x12\x44\n\x0bGetFeatures\x12\x15.sqwak.AudioFileChunk\x1a\x1a.sqwak.FeatureListResponse\"\x00(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AUDIOFILECHUNK = _descriptor.Descriptor(
  name='AudioFileChunk',
  full_name='sqwak.AudioFileChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='sqwak.AudioFileChunk.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=63,
)


_FEATURELISTRESPONSE = _descriptor.Descriptor(
  name='FeatureListResponse',
  full_name='sqwak.FeatureListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_vector', full_name='sqwak.FeatureListResponse.feature_vector', index=0,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['AudioFileChunk'] = _AUDIOFILECHUNK
DESCRIPTOR.message_types_by_name['FeatureListResponse'] = _FEATURELISTRESPONSE

AudioFileChunk = _reflection.GeneratedProtocolMessageType('AudioFileChunk', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOFILECHUNK,
  __module__ = 'FeatureExtractor_pb2'
  # @@protoc_insertion_point(class_scope:sqwak.AudioFileChunk)
  ))
_sym_db.RegisterMessage(AudioFileChunk)

FeatureListResponse = _reflection.GeneratedProtocolMessageType('FeatureListResponse', (_message.Message,), dict(
  DESCRIPTOR = _FEATURELISTRESPONSE,
  __module__ = 'FeatureExtractor_pb2'
  # @@protoc_insertion_point(class_scope:sqwak.FeatureListResponse)
  ))
_sym_db.RegisterMessage(FeatureListResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class Feature_ExtractorStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetFeatures = channel.stream_unary(
          '/sqwak.Feature_Extractor/GetFeatures',
          request_serializer=AudioFileChunk.SerializeToString,
          response_deserializer=FeatureListResponse.FromString,
          )


  class Feature_ExtractorServicer(object):

    def GetFeatures(self, request_iterator, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_Feature_ExtractorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetFeatures': grpc.stream_unary_rpc_method_handler(
            servicer.GetFeatures,
            request_deserializer=AudioFileChunk.FromString,
            response_serializer=FeatureListResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'sqwak.Feature_Extractor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaFeature_ExtractorServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetFeatures(self, request_iterator, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaFeature_ExtractorStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetFeatures(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetFeatures.future = None


  def beta_create_Feature_Extractor_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('sqwak.Feature_Extractor', 'GetFeatures'): AudioFileChunk.FromString,
    }
    response_serializers = {
      ('sqwak.Feature_Extractor', 'GetFeatures'): FeatureListResponse.SerializeToString,
    }
    method_implementations = {
      ('sqwak.Feature_Extractor', 'GetFeatures'): face_utilities.stream_unary_inline(servicer.GetFeatures),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Feature_Extractor_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('sqwak.Feature_Extractor', 'GetFeatures'): AudioFileChunk.SerializeToString,
    }
    response_deserializers = {
      ('sqwak.Feature_Extractor', 'GetFeatures'): FeatureListResponse.FromString,
    }
    cardinalities = {
      'GetFeatures': cardinality.Cardinality.STREAM_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'sqwak.Feature_Extractor', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
