import grpc

import komputer_client.komputer_pb2 as komputer_pb2
import komputer_client.komputer_pb2_grpc as komputer_pb2_grpc


class KomputerClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50053")
        self.stub = komputer_pb2_grpc.KomputerServiceStub(self.channel)

    def get_komputers(self):
        try:
            response = self.stub.List(komputer_pb2.KomputerListRequest())
            return [
                {
                    "id": komputer.id,
                    "name": komputer.name,
                    "description": komputer.description,
                    "price": komputer.price,
                    "image_url": komputer.image_url,
                    "stock": komputer.stock,
                }
                for komputer in response.komputers
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

    def create_komputer(self, komputer):
        try:
            response = self.stub.Create(
                komputer_pb2.KomputerCreateRequest(
                    name=komputer.name,
                    description=komputer.description,
                    price=komputer.price,
                    image_url=komputer.image_url,
                    stock=komputer.stock,
                )
            )

            return dict(
                name=response.komputer.name,
                description=response.komputer.description,
                price=response.komputer.price,
                image_url=response.komputer.image_url,
                stock=response.komputer.stock,
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

    def get_komputer(self, id):
        try:
            response = self.stub.Get(komputer_pb2.KomputerRequest(id=id))

            return dict(
                id=response.komputer.id,
                name=response.komputer.name,
                description=response.komputer.description,
                price=response.komputer.price,
                image_url=response.komputer.image_url,
                stock=response.komputer.stock,
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

    def update_komputer(self, komputer):
        try:
            response = self.stub.Update(
                komputer_pb2.KomputerUpdateRequest(
                    id=komputer.id,
                    name=komputer.name,
                    description=komputer.description,
                    price=komputer.price,
                    image_url=komputer.image_url,
                    stock=komputer.stock,
                )
            )

            return dict(
                name=response.komputer.name,
                description=response.komputer.description,
                price=response.komputer.price,
                image_url=response.komputer.image_url,
                stock=response.komputer.stock,
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

    def delete_komputer(self, id):
        try:
            response = self.stub.Delete(komputer_pb2.KomputerDeleteRequest(id=id))

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
