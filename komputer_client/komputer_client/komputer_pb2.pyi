from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Komputer(_message.Message):
    __slots__ = ("id", "name", "description", "price", "image_url", "stock")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class KomputerListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KomputerListResponse(_message.Message):
    __slots__ = ("komputers",)
    KOMPUTERS_FIELD_NUMBER: _ClassVar[int]
    komputers: _containers.RepeatedCompositeFieldContainer[Komputer]
    def __init__(self, komputers: _Optional[_Iterable[_Union[Komputer, _Mapping]]] = ...) -> None: ...

class KomputerRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KomputerResponse(_message.Message):
    __slots__ = ("komputer",)
    KOMPUTER_FIELD_NUMBER: _ClassVar[int]
    komputer: Komputer
    def __init__(self, komputer: _Optional[_Union[Komputer, _Mapping]] = ...) -> None: ...

class KomputerCreateRequest(_message.Message):
    __slots__ = ("name", "description", "price", "image_url", "stock")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class KomputerCreateResponse(_message.Message):
    __slots__ = ("komputer",)
    KOMPUTER_FIELD_NUMBER: _ClassVar[int]
    komputer: Komputer
    def __init__(self, komputer: _Optional[_Union[Komputer, _Mapping]] = ...) -> None: ...

class KomputerUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "description", "price", "image_url", "stock")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., image_url: _Optional[str] = ..., stock: _Optional[int] = ...) -> None: ...

class KomputerUpdateResponse(_message.Message):
    __slots__ = ("komputer",)
    KOMPUTER_FIELD_NUMBER: _ClassVar[int]
    komputer: Komputer
    def __init__(self, komputer: _Optional[_Union[Komputer, _Mapping]] = ...) -> None: ...

class KomputerDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KomputerDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
