import grpc

import client.buku_pb2 as buku_pb2
import client.buku_pb2_grpc as buku_pb2_grpc


class BukuClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50052")
        self.stub = buku_pb2_grpc.BukuServiceStub(self.channel)

    def get_bukus(self):
        try:
            response = self.stub.List(buku_pb2.BukuListRequest())
            return [
                {
                    "id": buku.id,
                    "name": buku.name,
                    "description": buku.description,
                    "price": buku.price,
                    "image_url": buku.image_url,
                    "stock": buku.stock,
                }
                for buku in response.bukus
            ]

        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def create_buku(self, buku):
        try:
            response = self.stub.Create(
                buku_pb2.BukuCreateRequest(
                    name=buku.name,
                    description=buku.description,
                    price=buku.price,
                    image_url=buku.image_url,
                    stock=buku.stock,
                )
            )

            return dict(
                name=response.buku.name,
                description=response.buku.description,
                price=response.buku.price,
                image_url=response.buku.image_url,
                stock=response.buku.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def get_buku(self, id):
        try:
            response = self.stub.Get(buku_pb2.BukuRequest(id=id))

            return dict(
                id=response.buku.id,
                name=response.buku.name,
                description=response.buku.description,
                price=response.buku.price,
                image_url=response.buku.image_url,
                stock=response.buku.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def update_buku(self, buku):
        try:
            response = self.stub.Update(
                buku_pb2.BukuUpdateRequest(
                    id=buku.id,
                    name=buku.name,
                    description=buku.description,
                    price=buku.price,
                    image_url=buku.image_url,
                    stock=buku.stock,
                )
            )

            return dict(
                name=response.buku.name,
                description=response.buku.description,
                price=response.buku.price,
                image_url=response.buku.image_url,
                stock=response.buku.stock,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )

    def delete_buku(self, id):
        try:
            response = self.stub.Delete(buku_pb2.BukuDeleteRequest(id=id))

            return dict(
                message=response.message,
            )
        except grpc.RpcError as e:
            print(e.details())
            return dict(
                error=dict(
                    code=e.code(),
                    message=e.details(),
                    details=e.debug_error_string(),
                )
            )
