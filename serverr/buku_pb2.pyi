from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Buku(_message.Message):
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

class BukuListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukuListResponse(_message.Message):
    __slots__ = ("bukus",)
    BUKUS_FIELD_NUMBER: _ClassVar[int]
    bukus: _containers.RepeatedCompositeFieldContainer[Buku]
    def __init__(self, bukus: _Optional[_Iterable[_Union[Buku, _Mapping]]] = ...) -> None: ...

class BukuRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BukuResponse(_message.Message):
    __slots__ = ("buku",)
    BUKU_FIELD_NUMBER: _ClassVar[int]
    buku: Buku
    def __init__(self, buku: _Optional[_Union[Buku, _Mapping]] = ...) -> None: ...

class BukuCreateRequest(_message.Message):
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

class BukuCreateResponse(_message.Message):
    __slots__ = ("buku",)
    BUKU_FIELD_NUMBER: _ClassVar[int]
    buku: Buku
    def __init__(self, buku: _Optional[_Union[Buku, _Mapping]] = ...) -> None: ...

class BukuUpdateRequest(_message.Message):
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

class BukuUpdateResponse(_message.Message):
    __slots__ = ("buku",)
    BUKU_FIELD_NUMBER: _ClassVar[int]
    buku: Buku
    def __init__(self, buku: _Optional[_Union[Buku, _Mapping]] = ...) -> None: ...

class BukuDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BukuDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
