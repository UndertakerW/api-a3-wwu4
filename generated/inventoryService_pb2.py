# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inventoryService.proto',
  package='inventoryService',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16inventoryService.proto\x12\x10inventoryService\x1a\nbook.proto\",\n\x0f\x43reateBookInput\x12\x19\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0b.books.Book\"5\n\x12\x43reateBookResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2k\n\x10InventoryService\x12W\n\nCreateBook\x12!.inventoryService.CreateBookInput\x1a$.inventoryService.CreateBookResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[book__pb2.DESCRIPTOR,])




_CREATEBOOKINPUT = _descriptor.Descriptor(
  name='CreateBookInput',
  full_name='inventoryService.CreateBookInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='inventoryService.CreateBookInput.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=100,
)


_CREATEBOOKRESPONSE = _descriptor.Descriptor(
  name='CreateBookResponse',
  full_name='inventoryService.CreateBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='inventoryService.CreateBookResponse.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='inventoryService.CreateBookResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=155,
)

_CREATEBOOKINPUT.fields_by_name['book'].message_type = book__pb2._BOOK
DESCRIPTOR.message_types_by_name['CreateBookInput'] = _CREATEBOOKINPUT
DESCRIPTOR.message_types_by_name['CreateBookResponse'] = _CREATEBOOKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBookInput = _reflection.GeneratedProtocolMessageType('CreateBookInput', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOOKINPUT,
  '__module__' : 'inventoryService_pb2'
  # @@protoc_insertion_point(class_scope:inventoryService.CreateBookInput)
  })
_sym_db.RegisterMessage(CreateBookInput)

CreateBookResponse = _reflection.GeneratedProtocolMessageType('CreateBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOOKRESPONSE,
  '__module__' : 'inventoryService_pb2'
  # @@protoc_insertion_point(class_scope:inventoryService.CreateBookResponse)
  })
_sym_db.RegisterMessage(CreateBookResponse)



_INVENTORYSERVICE = _descriptor.ServiceDescriptor(
  name='InventoryService',
  full_name='inventoryService.InventoryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=157,
  serialized_end=264,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBook',
    full_name='inventoryService.InventoryService.CreateBook',
    index=0,
    containing_service=None,
    input_type=_CREATEBOOKINPUT,
    output_type=_CREATEBOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INVENTORYSERVICE)

DESCRIPTOR.services_by_name['InventoryService'] = _INVENTORYSERVICE

# @@protoc_insertion_point(module_scope)
