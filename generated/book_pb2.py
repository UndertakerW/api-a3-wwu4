# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='books',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbook.proto\x12\x05\x62ooks\"^\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1b\n\x05genre\x18\x04 \x01(\x0e\x32\x0c.books.Genre\x12\x0c\n\x04year\x18\x05 \x01(\x05*/\n\x05Genre\x12\x08\n\x04GEN0\x10\x00\x12\x08\n\x04GEN1\x10\x01\x12\x08\n\x04GEN2\x10\x02\x12\x08\n\x04GEN3\x10\x03\x62\x06proto3'
)

_GENRE = _descriptor.EnumDescriptor(
  name='Genre',
  full_name='books.Genre',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GEN0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEN1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEN2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEN3', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=117,
  serialized_end=164,
)
_sym_db.RegisterEnumDescriptor(_GENRE)

Genre = enum_type_wrapper.EnumTypeWrapper(_GENRE)
GEN0 = 0
GEN1 = 1
GEN2 = 2
GEN3 = 3



_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='books.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='books.Book.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='books.Book.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='books.Book.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='books.Book.genre', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='books.Book.year', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=21,
  serialized_end=115,
)

_BOOK.fields_by_name['genre'].enum_type = _GENRE
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.enum_types_by_name['Genre'] = _GENRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:books.Book)
  })
_sym_db.RegisterMessage(Book)


# @@protoc_insertion_point(module_scope)
