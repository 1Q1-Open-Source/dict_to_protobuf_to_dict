# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csample.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xd9\x03\n\x0bMainMessage\x12\r\n\x05\x61_str\x18\x01 \x01(\t\x12>\n\x13int_to_lst_ints_map\x18\x02 \x03(\x0b\x32!.MainMessage.IntToLstIntsMapEntry\x12\x1a\n\x07\x61n_enum\x18\x03 \x01(\x0e\x32\t.SomeEnum\x12\x0e\n\x06\x61n_int\x18\x04 \x01(\x05\x12\x10\n\x08lst_ints\x18\x05 \x03(\x05\x12=\n\x12str_to_message_map\x18\x06 \x03(\x0b\x32!.MainMessage.StrToMessageMapEntry\x12\x35\n\x0estr_to_int_map\x18\x07 \x03(\x0b\x32\x1d.MainMessage.StrToIntMapEntry\x1aJ\n\x14IntToLstIntsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.ListOfIntsMessage:\x02\x38\x01\x1aG\n\x14StrToMessageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.SomeSubMessage:\x02\x38\x01\x1a\x32\n\x10StrToIntMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"B\n\x0eSomeSubMessage\x12\r\n\x05\x61_str\x18\x01 \x01(\t\x12\x0e\n\x06\x61_long\x18\x02 \x01(\x03\x12\x11\n\tlst_longs\x18\x03 \x03(\x03\"%\n\x11ListOfIntsMessage\x12\x10\n\x08lst_ints\x18\x01 \x03(\x05\"\xa8\x01\n\x19MessageWithListOfMessages\x12?\n\x0clst_messages\x18\x01 \x03(\x0b\x32).MessageWithListOfMessages.SomeSubMessage\x1aJ\n\x0eSomeSubMessage\x12\r\n\x05\x61_str\x18\x01 \x01(\t\x12)\n\x08\x61_struct\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct*!\n\x08SomeEnum\x12\t\n\x05\x66irst\x10\x00\x12\n\n\x06second\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sample_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MAINMESSAGE_INTTOLSTINTSMAPENTRY']._options = None
  _globals['_MAINMESSAGE_INTTOLSTINTSMAPENTRY']._serialized_options = b'8\001'
  _globals['_MAINMESSAGE_STRTOMESSAGEMAPENTRY']._options = None
  _globals['_MAINMESSAGE_STRTOMESSAGEMAPENTRY']._serialized_options = b'8\001'
  _globals['_MAINMESSAGE_STRTOINTMAPENTRY']._options = None
  _globals['_MAINMESSAGE_STRTOINTMAPENTRY']._serialized_options = b'8\001'
  _globals['_SOMEENUM']._serialized_start=921
  _globals['_SOMEENUM']._serialized_end=954
  _globals['_MAINMESSAGE']._serialized_start=168
  _globals['_MAINMESSAGE']._serialized_end=641
  _globals['_MAINMESSAGE_INTTOLSTINTSMAPENTRY']._serialized_start=442
  _globals['_MAINMESSAGE_INTTOLSTINTSMAPENTRY']._serialized_end=516
  _globals['_MAINMESSAGE_STRTOMESSAGEMAPENTRY']._serialized_start=518
  _globals['_MAINMESSAGE_STRTOMESSAGEMAPENTRY']._serialized_end=589
  _globals['_MAINMESSAGE_STRTOINTMAPENTRY']._serialized_start=591
  _globals['_MAINMESSAGE_STRTOINTMAPENTRY']._serialized_end=641
  _globals['_SOMESUBMESSAGE']._serialized_start=643
  _globals['_SOMESUBMESSAGE']._serialized_end=709
  _globals['_LISTOFINTSMESSAGE']._serialized_start=711
  _globals['_LISTOFINTSMESSAGE']._serialized_end=748
  _globals['_MESSAGEWITHLISTOFMESSAGES']._serialized_start=751
  _globals['_MESSAGEWITHLISTOFMESSAGES']._serialized_end=919
  _globals['_MESSAGEWITHLISTOFMESSAGES_SOMESUBMESSAGE']._serialized_start=845
  _globals['_MESSAGEWITHLISTOFMESSAGES_SOMESUBMESSAGE']._serialized_end=919
# @@protoc_insertion_point(module_scope)
