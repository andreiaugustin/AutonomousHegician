# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oef_search.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="oef_search.proto",
    package="fetch.aea.OefSearch",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x10oef_search.proto\x12\x13\x66\x65tch.aea.OefSearch"\xc7\x0b\n\x10OefSearchMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12Q\n\toef_error\x18\x05 \x01(\x0b\x32<.fetch.aea.OefSearch.OefSearchMessage.Oef_Error_PerformativeH\x00\x12_\n\x10register_service\x18\x06 \x01(\x0b\x32\x43.fetch.aea.OefSearch.OefSearchMessage.Register_Service_PerformativeH\x00\x12Y\n\rsearch_result\x18\x07 \x01(\x0b\x32@.fetch.aea.OefSearch.OefSearchMessage.Search_Result_PerformativeH\x00\x12]\n\x0fsearch_services\x18\x08 \x01(\x0b\x32\x42.fetch.aea.OefSearch.OefSearchMessage.Search_Services_PerformativeH\x00\x12\x63\n\x12unregister_service\x18\t \x01(\x0b\x32\x45.fetch.aea.OefSearch.OefSearchMessage.Unregister_Service_PerformativeH\x00\x1a"\n\x0b\x44\x65scription\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\x0c\x1a\xd1\x01\n\x11OefErrorOperation\x12W\n\toef_error\x18\x01 \x01(\x0e\x32\x44.fetch.aea.OefSearch.OefSearchMessage.OefErrorOperation.OefErrorEnum"c\n\x0cOefErrorEnum\x12\x14\n\x10REGISTER_SERVICE\x10\x00\x12\x16\n\x12UNREGISTER_SERVICE\x10\x01\x12\x13\n\x0fSEARCH_SERVICES\x10\x02\x12\x10\n\x0cSEND_MESSAGE\x10\x03\x1a\x8b\x01\n\x05Query\x12\x0f\n\x05\x62ytes\x18\x01 \x01(\x0cH\x00\x12\x46\n\x07nothing\x18\x02 \x01(\x0b\x32\x33.fetch.aea.OefSearch.OefSearchMessage.Query.NothingH\x00\x12\x15\n\x0bquery_bytes\x18\x03 \x01(\x0cH\x00\x1a\t\n\x07NothingB\x07\n\x05query\x1ao\n\x1dRegister_Service_Performative\x12N\n\x13service_description\x18\x01 \x01(\x0b\x32\x31.fetch.aea.OefSearch.OefSearchMessage.Description\x1aq\n\x1fUnregister_Service_Performative\x12N\n\x13service_description\x18\x01 \x01(\x0b\x32\x31.fetch.aea.OefSearch.OefSearchMessage.Description\x1aZ\n\x1cSearch_Services_Performative\x12:\n\x05query\x18\x01 \x01(\x0b\x32+.fetch.aea.OefSearch.OefSearchMessage.Query\x1a,\n\x1aSearch_Result_Performative\x12\x0e\n\x06\x61gents\x18\x01 \x03(\t\x1an\n\x16Oef_Error_Performative\x12T\n\x13oef_error_operation\x18\x01 \x01(\x0b\x32\x37.fetch.aea.OefSearch.OefSearchMessage.OefErrorOperationB\x0e\n\x0cperformativeb\x06proto3',
)


_OEFSEARCHMESSAGE_OEFERROROPERATION_OEFERRORENUM = _descriptor.EnumDescriptor(
    name="OefErrorEnum",
    full_name="fetch.aea.OefSearch.OefSearchMessage.OefErrorOperation.OefErrorEnum",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="REGISTER_SERVICE",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNREGISTER_SERVICE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEARCH_SERVICES",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEND_MESSAGE", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=786,
    serialized_end=885,
)
_sym_db.RegisterEnumDescriptor(_OEFSEARCHMESSAGE_OEFERROROPERATION_OEFERRORENUM)


_OEFSEARCHMESSAGE_DESCRIPTION = _descriptor.Descriptor(
    name="Description",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Description",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="description",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Description.description",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
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
    serialized_start=639,
    serialized_end=673,
)

_OEFSEARCHMESSAGE_OEFERROROPERATION = _descriptor.Descriptor(
    name="OefErrorOperation",
    full_name="fetch.aea.OefSearch.OefSearchMessage.OefErrorOperation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="oef_error",
            full_name="fetch.aea.OefSearch.OefSearchMessage.OefErrorOperation.oef_error",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_OEFSEARCHMESSAGE_OEFERROROPERATION_OEFERRORENUM,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=676,
    serialized_end=885,
)

_OEFSEARCHMESSAGE_QUERY_NOTHING = _descriptor.Descriptor(
    name="Nothing",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Query.Nothing",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1009,
    serialized_end=1018,
)

_OEFSEARCHMESSAGE_QUERY = _descriptor.Descriptor(
    name="Query",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Query",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bytes",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Query.bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="nothing",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Query.nothing",
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
        ),
        _descriptor.FieldDescriptor(
            name="query_bytes",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Query.query_bytes",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_OEFSEARCHMESSAGE_QUERY_NOTHING,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="query",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Query.query",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=888,
    serialized_end=1027,
)

_OEFSEARCHMESSAGE_REGISTER_SERVICE_PERFORMATIVE = _descriptor.Descriptor(
    name="Register_Service_Performative",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Register_Service_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="service_description",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Register_Service_Performative.service_description",
            index=0,
            number=1,
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
    serialized_start=1029,
    serialized_end=1140,
)

_OEFSEARCHMESSAGE_UNREGISTER_SERVICE_PERFORMATIVE = _descriptor.Descriptor(
    name="Unregister_Service_Performative",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Unregister_Service_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="service_description",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Unregister_Service_Performative.service_description",
            index=0,
            number=1,
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
    serialized_start=1142,
    serialized_end=1255,
)

_OEFSEARCHMESSAGE_SEARCH_SERVICES_PERFORMATIVE = _descriptor.Descriptor(
    name="Search_Services_Performative",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Search_Services_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Search_Services_Performative.query",
            index=0,
            number=1,
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
    serialized_start=1257,
    serialized_end=1347,
)

_OEFSEARCHMESSAGE_SEARCH_RESULT_PERFORMATIVE = _descriptor.Descriptor(
    name="Search_Result_Performative",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Search_Result_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="agents",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Search_Result_Performative.agents",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
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
    serialized_start=1349,
    serialized_end=1393,
)

_OEFSEARCHMESSAGE_OEF_ERROR_PERFORMATIVE = _descriptor.Descriptor(
    name="Oef_Error_Performative",
    full_name="fetch.aea.OefSearch.OefSearchMessage.Oef_Error_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="oef_error_operation",
            full_name="fetch.aea.OefSearch.OefSearchMessage.Oef_Error_Performative.oef_error_operation",
            index=0,
            number=1,
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
    serialized_start=1395,
    serialized_end=1505,
)

_OEFSEARCHMESSAGE = _descriptor.Descriptor(
    name="OefSearchMessage",
    full_name="fetch.aea.OefSearch.OefSearchMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.OefSearch.OefSearchMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.OefSearch.OefSearchMessage.dialogue_starter_reference",
            index=1,
            number=2,
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
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.OefSearch.OefSearchMessage.dialogue_responder_reference",
            index=2,
            number=3,
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
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.OefSearch.OefSearchMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="oef_error",
            full_name="fetch.aea.OefSearch.OefSearchMessage.oef_error",
            index=4,
            number=5,
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
        ),
        _descriptor.FieldDescriptor(
            name="register_service",
            full_name="fetch.aea.OefSearch.OefSearchMessage.register_service",
            index=5,
            number=6,
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
        ),
        _descriptor.FieldDescriptor(
            name="search_result",
            full_name="fetch.aea.OefSearch.OefSearchMessage.search_result",
            index=6,
            number=7,
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
        ),
        _descriptor.FieldDescriptor(
            name="search_services",
            full_name="fetch.aea.OefSearch.OefSearchMessage.search_services",
            index=7,
            number=8,
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
        ),
        _descriptor.FieldDescriptor(
            name="unregister_service",
            full_name="fetch.aea.OefSearch.OefSearchMessage.unregister_service",
            index=8,
            number=9,
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
        ),
    ],
    extensions=[],
    nested_types=[
        _OEFSEARCHMESSAGE_DESCRIPTION,
        _OEFSEARCHMESSAGE_OEFERROROPERATION,
        _OEFSEARCHMESSAGE_QUERY,
        _OEFSEARCHMESSAGE_REGISTER_SERVICE_PERFORMATIVE,
        _OEFSEARCHMESSAGE_UNREGISTER_SERVICE_PERFORMATIVE,
        _OEFSEARCHMESSAGE_SEARCH_SERVICES_PERFORMATIVE,
        _OEFSEARCHMESSAGE_SEARCH_RESULT_PERFORMATIVE,
        _OEFSEARCHMESSAGE_OEF_ERROR_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.OefSearch.OefSearchMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=42,
    serialized_end=1521,
)

_OEFSEARCHMESSAGE_DESCRIPTION.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_OEFERROROPERATION.fields_by_name[
    "oef_error"
].enum_type = _OEFSEARCHMESSAGE_OEFERROROPERATION_OEFERRORENUM
_OEFSEARCHMESSAGE_OEFERROROPERATION.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_OEFERROROPERATION_OEFERRORENUM.containing_type = (
    _OEFSEARCHMESSAGE_OEFERROROPERATION
)
_OEFSEARCHMESSAGE_QUERY_NOTHING.containing_type = _OEFSEARCHMESSAGE_QUERY
_OEFSEARCHMESSAGE_QUERY.fields_by_name[
    "nothing"
].message_type = _OEFSEARCHMESSAGE_QUERY_NOTHING
_OEFSEARCHMESSAGE_QUERY.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _OEFSEARCHMESSAGE_QUERY.fields_by_name["bytes"]
)
_OEFSEARCHMESSAGE_QUERY.fields_by_name[
    "bytes"
].containing_oneof = _OEFSEARCHMESSAGE_QUERY.oneofs_by_name["query"]
_OEFSEARCHMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _OEFSEARCHMESSAGE_QUERY.fields_by_name["nothing"]
)
_OEFSEARCHMESSAGE_QUERY.fields_by_name[
    "nothing"
].containing_oneof = _OEFSEARCHMESSAGE_QUERY.oneofs_by_name["query"]
_OEFSEARCHMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _OEFSEARCHMESSAGE_QUERY.fields_by_name["query_bytes"]
)
_OEFSEARCHMESSAGE_QUERY.fields_by_name[
    "query_bytes"
].containing_oneof = _OEFSEARCHMESSAGE_QUERY.oneofs_by_name["query"]
_OEFSEARCHMESSAGE_REGISTER_SERVICE_PERFORMATIVE.fields_by_name[
    "service_description"
].message_type = _OEFSEARCHMESSAGE_DESCRIPTION
_OEFSEARCHMESSAGE_REGISTER_SERVICE_PERFORMATIVE.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_UNREGISTER_SERVICE_PERFORMATIVE.fields_by_name[
    "service_description"
].message_type = _OEFSEARCHMESSAGE_DESCRIPTION
_OEFSEARCHMESSAGE_UNREGISTER_SERVICE_PERFORMATIVE.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_SEARCH_SERVICES_PERFORMATIVE.fields_by_name[
    "query"
].message_type = _OEFSEARCHMESSAGE_QUERY
_OEFSEARCHMESSAGE_SEARCH_SERVICES_PERFORMATIVE.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_SEARCH_RESULT_PERFORMATIVE.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE_OEF_ERROR_PERFORMATIVE.fields_by_name[
    "oef_error_operation"
].message_type = _OEFSEARCHMESSAGE_OEFERROROPERATION
_OEFSEARCHMESSAGE_OEF_ERROR_PERFORMATIVE.containing_type = _OEFSEARCHMESSAGE
_OEFSEARCHMESSAGE.fields_by_name[
    "oef_error"
].message_type = _OEFSEARCHMESSAGE_OEF_ERROR_PERFORMATIVE
_OEFSEARCHMESSAGE.fields_by_name[
    "register_service"
].message_type = _OEFSEARCHMESSAGE_REGISTER_SERVICE_PERFORMATIVE
_OEFSEARCHMESSAGE.fields_by_name[
    "search_result"
].message_type = _OEFSEARCHMESSAGE_SEARCH_RESULT_PERFORMATIVE
_OEFSEARCHMESSAGE.fields_by_name[
    "search_services"
].message_type = _OEFSEARCHMESSAGE_SEARCH_SERVICES_PERFORMATIVE
_OEFSEARCHMESSAGE.fields_by_name[
    "unregister_service"
].message_type = _OEFSEARCHMESSAGE_UNREGISTER_SERVICE_PERFORMATIVE
_OEFSEARCHMESSAGE.oneofs_by_name["performative"].fields.append(
    _OEFSEARCHMESSAGE.fields_by_name["oef_error"]
)
_OEFSEARCHMESSAGE.fields_by_name[
    "oef_error"
].containing_oneof = _OEFSEARCHMESSAGE.oneofs_by_name["performative"]
_OEFSEARCHMESSAGE.oneofs_by_name["performative"].fields.append(
    _OEFSEARCHMESSAGE.fields_by_name["register_service"]
)
_OEFSEARCHMESSAGE.fields_by_name[
    "register_service"
].containing_oneof = _OEFSEARCHMESSAGE.oneofs_by_name["performative"]
_OEFSEARCHMESSAGE.oneofs_by_name["performative"].fields.append(
    _OEFSEARCHMESSAGE.fields_by_name["search_result"]
)
_OEFSEARCHMESSAGE.fields_by_name[
    "search_result"
].containing_oneof = _OEFSEARCHMESSAGE.oneofs_by_name["performative"]
_OEFSEARCHMESSAGE.oneofs_by_name["performative"].fields.append(
    _OEFSEARCHMESSAGE.fields_by_name["search_services"]
)
_OEFSEARCHMESSAGE.fields_by_name[
    "search_services"
].containing_oneof = _OEFSEARCHMESSAGE.oneofs_by_name["performative"]
_OEFSEARCHMESSAGE.oneofs_by_name["performative"].fields.append(
    _OEFSEARCHMESSAGE.fields_by_name["unregister_service"]
)
_OEFSEARCHMESSAGE.fields_by_name[
    "unregister_service"
].containing_oneof = _OEFSEARCHMESSAGE.oneofs_by_name["performative"]
DESCRIPTOR.message_types_by_name["OefSearchMessage"] = _OEFSEARCHMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OefSearchMessage = _reflection.GeneratedProtocolMessageType(
    "OefSearchMessage",
    (_message.Message,),
    {
        "Description": _reflection.GeneratedProtocolMessageType(
            "Description",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_DESCRIPTION,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Description)
            },
        ),
        "OefErrorOperation": _reflection.GeneratedProtocolMessageType(
            "OefErrorOperation",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_OEFERROROPERATION,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.OefErrorOperation)
            },
        ),
        "Query": _reflection.GeneratedProtocolMessageType(
            "Query",
            (_message.Message,),
            {
                "Nothing": _reflection.GeneratedProtocolMessageType(
                    "Nothing",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _OEFSEARCHMESSAGE_QUERY_NOTHING,
                        "__module__": "oef_search_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Query.Nothing)
                    },
                ),
                "DESCRIPTOR": _OEFSEARCHMESSAGE_QUERY,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Query)
            },
        ),
        "Register_Service_Performative": _reflection.GeneratedProtocolMessageType(
            "Register_Service_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_REGISTER_SERVICE_PERFORMATIVE,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Register_Service_Performative)
            },
        ),
        "Unregister_Service_Performative": _reflection.GeneratedProtocolMessageType(
            "Unregister_Service_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_UNREGISTER_SERVICE_PERFORMATIVE,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Unregister_Service_Performative)
            },
        ),
        "Search_Services_Performative": _reflection.GeneratedProtocolMessageType(
            "Search_Services_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_SEARCH_SERVICES_PERFORMATIVE,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Search_Services_Performative)
            },
        ),
        "Search_Result_Performative": _reflection.GeneratedProtocolMessageType(
            "Search_Result_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_SEARCH_RESULT_PERFORMATIVE,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Search_Result_Performative)
            },
        ),
        "Oef_Error_Performative": _reflection.GeneratedProtocolMessageType(
            "Oef_Error_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _OEFSEARCHMESSAGE_OEF_ERROR_PERFORMATIVE,
                "__module__": "oef_search_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage.Oef_Error_Performative)
            },
        ),
        "DESCRIPTOR": _OEFSEARCHMESSAGE,
        "__module__": "oef_search_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.OefSearch.OefSearchMessage)
    },
)
_sym_db.RegisterMessage(OefSearchMessage)
_sym_db.RegisterMessage(OefSearchMessage.Description)
_sym_db.RegisterMessage(OefSearchMessage.OefErrorOperation)
_sym_db.RegisterMessage(OefSearchMessage.Query)
_sym_db.RegisterMessage(OefSearchMessage.Query.Nothing)
_sym_db.RegisterMessage(OefSearchMessage.Register_Service_Performative)
_sym_db.RegisterMessage(OefSearchMessage.Unregister_Service_Performative)
_sym_db.RegisterMessage(OefSearchMessage.Search_Services_Performative)
_sym_db.RegisterMessage(OefSearchMessage.Search_Result_Performative)
_sym_db.RegisterMessage(OefSearchMessage.Oef_Error_Performative)


# @@protoc_insertion_point(module_scope)
