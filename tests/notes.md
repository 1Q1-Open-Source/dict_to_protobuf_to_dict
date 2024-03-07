I need to build a better test matrix so I can drive this with hypothesis.

.proto Type Matrix Notes

field variations:
    optional fields (if optional and not specified the value is the default value)
    repeated fields (if not specified the value is an empty list)
    Oneof fields
    Map fields 
        KEY: int32, int64, uint32, uint64, sint32, sint64, fixed32, fixed64, sfixed32, sfixed64, bool, string
        VALUE: any type except for another map

the combinations of 54 items = 2^54 = 18,014,398,509,481,984
This is too many to write tests for. I need to find a way to generate tests for this.

Scalar types:
    double		
    repeated double		
    float		
    repeated float		
    int32
    repeated int32
    int64
    repeated int64
    uint32
    repeated uint32
    uint64
    repeated uint64
    sint32
    repeated sint32
    sint64
    repeated sint64
    fixed32
    repeated fixed32
    fixed64
    repeated fixed64
    sfixed32
    repeated sfixed32
    sfixed64
    repeated sfixed64
    bool
    repeated bool
    string
    repeated string
    bytes
    repeated bytes
    the example enum without reserved values
    the example enum without reserved values
    the example enum with reserved values
    the example enum with reserved values
    Any (message) (import "google/protobuf/any.proto";)
    Any (message) (import "google/protobuf/any.proto";)
    Api (message) (import "google/protobuf/api.proto";)
    Api (message) (import "google/protobuf/api.proto";)
    Duration (message) (import "google/protobuf/duration.proto";)
    Duration (message) (import "google/protobuf/duration.proto";)
    Empty (message) (import "google/protobuf/empty.proto";)
    Empty (message) (import "google/protobuf/empty.proto";)
    Enum (message) (import "google/protobuf/type.proto";)
    Enum (message) (import "google/protobuf/type.proto";)
    Field (message) (import "google/protobuf/type.proto";)
    Field (message) (import "google/protobuf/type.proto";)
    FieldMask (message) (import "google/protobuf/field_mask.proto";)
    FieldMask (message) (import "google/protobuf/field_mask.proto";)
    Struct (message) (import "google/protobuf/struct.proto";)
    Struct (message) (import "google/protobuf/struct.proto";)
    Timestamp (message) (import "google/protobuf/timestamp.proto";)
    Timestamp (message) (import "google/protobuf/timestamp.proto";)
    Type (message) (import "google/protobuf/type.proto";)
    Type (message) (import "google/protobuf/type.proto";)
        Method (message) (import "google/protobuf/api.proto";)  
        Method (message) (import "google/protobuf/api.proto";)  
        Method (message) (import "google/protobuf/api.proto";)  
        Option (message) (import "google/protobuf/type.proto";)
        Option (message) (import "google/protobuf/type.proto";)
        Option (message) (import "google/protobuf/type.proto";)
        SourceContext (message) (import "google/protobuf/source_context.proto";)
        SourceContext (message) (import "google/protobuf/source_context.proto";)
        SourceContext (message) (import "google/protobuf/source_context.proto";)
        Mixin (message) (import "google/protobuf/api.proto";)
        Mixin (message) (import "google/protobuf/api.proto";)
        Mixin (message) (import "google/protobuf/api.proto";)
        Syntax (enum) (import "google/protobuf/type.proto";)
        Syntax (enum) (import "google/protobuf/type.proto";)
        Syntax (enum) (import "google/protobuf/type.proto";)
        EnumValue (message) (import "google/protobuf/type.proto";)
        EnumValue (message) (import "google/protobuf/type.proto";)
        EnumValue (message) (import "google/protobuf/type.proto";)
        Field.Cardinality (enum) (import "google/protobuf/type.proto";)
        Field.Cardinality (enum) (import "google/protobuf/type.proto";)
        Field.Cardinality (enum) (import "google/protobuf/type.proto";)
        Field.Kind (enum) (import "google/protobuf/type.proto";)
        Field.Kind (enum) (import "google/protobuf/type.proto";)
        Field.Kind (enum) (import "google/protobuf/type.proto";)
        NullValue (enum) (import "google/protobuf/struct.proto";)
        NullValue (enum) (import "google/protobuf/struct.proto";)
        NullValue (enum) (import "google/protobuf/struct.proto";)
        ListValue (message) (import "google/protobuf/struct.proto";)
        ListValue (message) (import "google/protobuf/struct.proto";)
        ListValue (message) (import "google/protobuf/struct.proto";)
        Value (message) (import "google/protobuf/struct.proto";)
        Value (message) (import "google/protobuf/struct.proto";)
        Value (message) (import "google/protobuf/struct.proto";)


    BoolValue (message) (import "google/protobuf/wrappers.proto";)
    BoolValue (message) (import "google/protobuf/wrappers.proto";)
    BoolValue (message) (import "google/protobuf/wrappers.proto";)
    BytesValue (message) (import "google/protobuf/wrappers.proto";)
    BytesValue (message) (import "google/protobuf/wrappers.proto";)
    BytesValue (message) (import "google/protobuf/wrappers.proto";)
    DoubleValue (message) (import "google/protobuf/wrappers.proto";)
    DoubleValue (message) (import "google/protobuf/wrappers.proto";)
    DoubleValue (message) (import "google/protobuf/wrappers.proto";)
    FloatValue (message) (import "google/protobuf/wrappers.proto";)
    FloatValue (message) (import "google/protobuf/wrappers.proto";)
    FloatValue (message) (import "google/protobuf/wrappers.proto";)
    Int32Value (message) (import "google/protobuf/wrappers.proto";)
    Int32Value (message) (import "google/protobuf/wrappers.proto";)
    Int32Value (message) (import "google/protobuf/wrappers.proto";)
    Int64Value (message) (import "google/protobuf/wrappers.proto";)
    Int64Value (message) (import "google/protobuf/wrappers.proto";)
    Int64Value (message) (import "google/protobuf/wrappers.proto";)
    StringValue (message) (import "google/protobuf/wrappers.proto";)
    StringValue (message) (import "google/protobuf/wrappers.proto";)
    StringValue (message) (import "google/protobuf/wrappers.proto";)
    UInt32Value (message) (import "google/protobuf/wrappers.proto";)
    UInt32Value (message) (import "google/protobuf/wrappers.proto";)
    UInt32Value (message) (import "google/protobuf/wrappers.proto";)
    UInt64Value (message) (import "google/protobuf/wrappers.proto";)
    UInt64Value (message) (import "google/protobuf/wrappers.proto";)
    UInt64Value (message) (import "google/protobuf/wrappers.proto";)
    
    
    