from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SomeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    first: _ClassVar[SomeEnum]
    second: _ClassVar[SomeEnum]
first: SomeEnum
second: SomeEnum

class MainMessage(_message.Message):
    __slots__ = ("a_str", "int_to_lst_ints_map", "an_enum", "an_int", "lst_ints", "str_to_message_map", "str_to_int_map")
    class IntToLstIntsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ListOfIntsMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ListOfIntsMessage, _Mapping]] = ...) -> None: ...
    class StrToMessageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SomeSubMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SomeSubMessage, _Mapping]] = ...) -> None: ...
    class StrToIntMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    A_STR_FIELD_NUMBER: _ClassVar[int]
    INT_TO_LST_INTS_MAP_FIELD_NUMBER: _ClassVar[int]
    AN_ENUM_FIELD_NUMBER: _ClassVar[int]
    AN_INT_FIELD_NUMBER: _ClassVar[int]
    LST_INTS_FIELD_NUMBER: _ClassVar[int]
    STR_TO_MESSAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    STR_TO_INT_MAP_FIELD_NUMBER: _ClassVar[int]
    a_str: str
    int_to_lst_ints_map: _containers.MessageMap[int, ListOfIntsMessage]
    an_enum: SomeEnum
    an_int: int
    lst_ints: _containers.RepeatedScalarFieldContainer[int]
    str_to_message_map: _containers.MessageMap[str, SomeSubMessage]
    str_to_int_map: _containers.ScalarMap[str, int]
    def __init__(self, a_str: _Optional[str] = ..., int_to_lst_ints_map: _Optional[_Mapping[int, ListOfIntsMessage]] = ..., an_enum: _Optional[_Union[SomeEnum, str]] = ..., an_int: _Optional[int] = ..., lst_ints: _Optional[_Iterable[int]] = ..., str_to_message_map: _Optional[_Mapping[str, SomeSubMessage]] = ..., str_to_int_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class SomeSubMessage(_message.Message):
    __slots__ = ("a_str", "a_long", "lst_longs")
    A_STR_FIELD_NUMBER: _ClassVar[int]
    A_LONG_FIELD_NUMBER: _ClassVar[int]
    LST_LONGS_FIELD_NUMBER: _ClassVar[int]
    a_str: str
    a_long: int
    lst_longs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, a_str: _Optional[str] = ..., a_long: _Optional[int] = ..., lst_longs: _Optional[_Iterable[int]] = ...) -> None: ...

class ListOfIntsMessage(_message.Message):
    __slots__ = ("lst_ints",)
    LST_INTS_FIELD_NUMBER: _ClassVar[int]
    lst_ints: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, lst_ints: _Optional[_Iterable[int]] = ...) -> None: ...

class MessageWithListOfMessages(_message.Message):
    __slots__ = ("lst_messages",)
    class SomeSubMessage(_message.Message):
        __slots__ = ("a_str", "a_struct")
        A_STR_FIELD_NUMBER: _ClassVar[int]
        A_STRUCT_FIELD_NUMBER: _ClassVar[int]
        a_str: str
        a_struct: _struct_pb2.Struct
        def __init__(self, a_str: _Optional[str] = ..., a_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    LST_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    lst_messages: _containers.RepeatedCompositeFieldContainer[MessageWithListOfMessages.SomeSubMessage]
    def __init__(self, lst_messages: _Optional[_Iterable[_Union[MessageWithListOfMessages.SomeSubMessage, _Mapping]]] = ...) -> None: ...
