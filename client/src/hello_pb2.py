# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hello.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'hello.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x05hello\"0\n\x11NewProductRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x05\"%\n\x12NewProductResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32U\n\x0eProductService\x12\x43\n\nNewProduct\x12\x18.hello.NewProductRequest\x1a\x19.hello.NewProductResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NEWPRODUCTREQUEST']._serialized_start=22
  _globals['_NEWPRODUCTREQUEST']._serialized_end=70
  _globals['_NEWPRODUCTRESPONSE']._serialized_start=72
  _globals['_NEWPRODUCTRESPONSE']._serialized_end=109
  _globals['_PRODUCTSERVICE']._serialized_start=111
  _globals['_PRODUCTSERVICE']._serialized_end=196
# @@protoc_insertion_point(module_scope)
