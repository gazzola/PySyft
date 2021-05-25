# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/adp/entity.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# syft absolute
from syft.proto.core.common import \
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/adp/entity.proto",
    package="syft.core.adp",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bproto/core/adp/entity.proto\x12\rsyft.core.adp\x1a%proto/core/common/common_object.proto"@\n\x06\x45ntity\x12\x13\n\x0bunique_name\x18\x01 \x01(\t\x12!\n\x02id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_ENTITY = _descriptor.Descriptor(
    name="Entity",
    full_name="syft.core.adp.Entity",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="unique_name",
            full_name="syft.core.adp.Entity.unique_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.core.adp.Entity.id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=85,
    serialized_end=149,
)

_ENTITY.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["Entity"] = _ENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType(
    "Entity",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENTITY,
        "__module__": "proto.core.adp.entity_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.adp.Entity)
    },
)
_sym_db.RegisterMessage(Entity)


# @@protoc_insertion_point(module_scope)
