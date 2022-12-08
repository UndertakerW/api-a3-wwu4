# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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
  serialized_pb=b'\n\x16inventoryService.proto\x12\x10inventoryService\x1a\nbook.proto\".\n\x11\x43reateBookRequest\x12\x19\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0b.books.Book\"Y\n\x12\x43reateBookResponse\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".inventoryService.CreateBookStatus\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\",\n\x0fGetBookResponse\x12\x19\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0b.books.Book*\x82\x01\n\x10\x43reateBookStatus\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0e\n\nISBN_ERROR\x10\x02\x12\x0f\n\x0bTITLE_ERROR\x10\x03\x12\x10\n\x0c\x41UTHOR_ERROR\x10\x04\x12\x0f\n\x0bGENRE_ERROR\x10\x05\x12\x0e\n\nYEAR_ERROR\x10\x06\x32\xc2\x01\n\x10InventoryService\x12Y\n\nCreateBook\x12#.inventoryService.CreateBookRequest\x1a$.inventoryService.CreateBookResponse\"\x00\x12S\n\x07GetBook\x12 .inventoryService.GetBookRequest\x1a$.inventoryService.CreateBookResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[book__pb2.DESCRIPTOR,])

_CREATEBOOKSTATUS = _descriptor.EnumDescriptor(
  name='CreateBookStatus',
  full_name='inventoryService.CreateBookStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ISBN_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TITLE_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHOR_ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GENRE_ERROR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YEAR_ERROR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=274,
  serialized_end=404,
)
_sym_db.RegisterEnumDescriptor(_CREATEBOOKSTATUS)

CreateBookStatus = enum_type_wrapper.EnumTypeWrapper(_CREATEBOOKSTATUS)
UNDEFINED = 0
SUCCESS = 1
ISBN_ERROR = 2
TITLE_ERROR = 3
AUTHOR_ERROR = 4
GENRE_ERROR = 5
YEAR_ERROR = 6



_CREATEBOOKREQUEST = _descriptor.Descriptor(
  name='CreateBookRequest',
  full_name='inventoryService.CreateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='inventoryService.CreateBookRequest.book', index=0,
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
  serialized_end=102,
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
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=104,
  serialized_end=193,
)


_GETBOOKREQUEST = _descriptor.Descriptor(
  name='GetBookRequest',
  full_name='inventoryService.GetBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='inventoryService.GetBookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=195,
  serialized_end=225,
)


_GETBOOKRESPONSE = _descriptor.Descriptor(
  name='GetBookResponse',
  full_name='inventoryService.GetBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='inventoryService.GetBookResponse.book', index=0,
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
  serialized_start=227,
  serialized_end=271,
)

_CREATEBOOKREQUEST.fields_by_name['book'].message_type = book__pb2._BOOK
_CREATEBOOKRESPONSE.fields_by_name['status'].enum_type = _CREATEBOOKSTATUS
_GETBOOKRESPONSE.fields_by_name['book'].message_type = book__pb2._BOOK
DESCRIPTOR.message_types_by_name['CreateBookRequest'] = _CREATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['CreateBookResponse'] = _CREATEBOOKRESPONSE
DESCRIPTOR.message_types_by_name['GetBookRequest'] = _GETBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookResponse'] = _GETBOOKRESPONSE
DESCRIPTOR.enum_types_by_name['CreateBookStatus'] = _CREATEBOOKSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBookRequest = _reflection.GeneratedProtocolMessageType('CreateBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOOKREQUEST,
  '__module__' : 'inventoryService_pb2'
  # @@protoc_insertion_point(class_scope:inventoryService.CreateBookRequest)
  })
_sym_db.RegisterMessage(CreateBookRequest)

CreateBookResponse = _reflection.GeneratedProtocolMessageType('CreateBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOOKRESPONSE,
  '__module__' : 'inventoryService_pb2'
  # @@protoc_insertion_point(class_scope:inventoryService.CreateBookResponse)
  })
_sym_db.RegisterMessage(CreateBookResponse)

GetBookRequest = _reflection.GeneratedProtocolMessageType('GetBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKREQUEST,
  '__module__' : 'inventoryService_pb2'
  # @@protoc_insertion_point(class_scope:inventoryService.GetBookRequest)
  })
_sym_db.RegisterMessage(GetBookRequest)

GetBookResponse = _reflection.GeneratedProtocolMessageType('GetBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKRESPONSE,
  '__module__' : 'inventoryService_pb2'
  # @@protoc_insertion_point(class_scope:inventoryService.GetBookResponse)
  })
_sym_db.RegisterMessage(GetBookResponse)



_INVENTORYSERVICE = _descriptor.ServiceDescriptor(
  name='InventoryService',
  full_name='inventoryService.InventoryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=407,
  serialized_end=601,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBook',
    full_name='inventoryService.InventoryService.CreateBook',
    index=0,
    containing_service=None,
    input_type=_CREATEBOOKREQUEST,
    output_type=_CREATEBOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='inventoryService.InventoryService.GetBook',
    index=1,
    containing_service=None,
    input_type=_GETBOOKREQUEST,
    output_type=_CREATEBOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_INVENTORYSERVICE)

DESCRIPTOR.services_by_name['InventoryService'] = _INVENTORYSERVICE

# @@protoc_insertion_point(module_scope)
