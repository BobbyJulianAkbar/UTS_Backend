from concurrent import futures
import time
import logging
import grpc

import traceback

import komputer_pb2
import komputer_pb2_grpc

from komputer import Komputer
from sqlalchemy import create_engine, insert, select, update, delete

engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/utsbackendjo")


class KomputerService(komputer_pb2_grpc.KomputerServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                komputers = conn.execute(select(Komputer)).all()

                return komputer_pb2.KomputerListResponse(
                    komputers=[
                        komputer_pb2.Komputer(
                            id=komputer.id,
                            name=komputer.name,
                            description=komputer.description,
                            price=komputer.price,
                            image_url=komputer.image_url,
                            stock=komputer.stock,
                        )
                        for komputer in komputers
                    ]
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return komputer_pb2.KomputerListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    insert(Komputer),
                    [
                        {
                            "name": request.name,
                            "description": request.description,
                            "price": request.price,
                            "image_url": request.image_url,
                            "stock": request.stock,
                        }
                    ],
                )

                conn.commit()

                return komputer_pb2.KomputerCreateResponse(
                    komputer=komputer_pb2.Komputer(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return komputer_pb2.KomputerCreateResponse()

    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                komputer = conn.execute(
                    select(Komputer).where(Komputer.id == request.id)
                ).first()

                if komputer is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("komputer not found")
                    return komputer_pb2.KomputerResponse()

                return komputer_pb2.KomputerResponse(
                    komputer=komputer_pb2.Komputer(
                        id=komputer.id,
                        name=komputer.name,
                        description=komputer.description,
                        price=komputer.price,
                        image_url=komputer.image_url,
                        stock=komputer.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return komputer_pb2.KomputerResponse()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    update(Komputer)
                    .where(Komputer.id == request.id)
                    .values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )

                conn.commit()

                return komputer_pb2.KomputerUpdateResponse(
                    komputer=komputer_pb2.Komputer(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return komputer_pb2.KomputerUpdateResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(delete(Komputer).where(Komputer.id == request.id))

                conn.commit()

                return komputer_pb2.KomputerDeleteResponse(
                    message="komputer deleted successfully"
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return komputer_pb2.KomputerDeleteResponse()


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    komputer_pb2_grpc.add_KomputerServiceServicer_to_server(KomputerService(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("Server started at port 50053")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    server()
