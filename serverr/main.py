from concurrent import futures
import time
import logging
import grpc

import traceback

import buku_pb2
import buku_pb2_grpc

from buku import Buku
from sqlalchemy import create_engine, insert, text, values, select, update, delete, desc

engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/utsbo")


class BukuService(buku_pb2_grpc.BukuServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                bukus = conn.execute(select(Buku)).all()

                return buku_pb2.BukuListResponse(
                    bukus=[
                        buku_pb2.Buku(
                            id=buku.id,
                            name=buku.name,
                            description=buku.description,
                            price=buku.price,
                            image_url=buku.image_url,
                            stock=buku.stock,
                        )
                        for buku in bukus
                    ]
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return buku_pb2.BukuListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    insert(Buku),
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

                return buku_pb2.BukuCreateResponse(
                    buku=buku_pb2.Buku(
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
            return buku_pb2.BukuCreateResponse()

    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                buku = conn.execute(select(Buku).where(Buku.id == request.id)).first()

                if buku is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("buku not found")
                    return buku_pb2.BukuResponse()

                return buku_pb2.BukuResponse(
                    buku=buku_pb2.Buku(
                        id=buku.id,
                        name=buku.name,
                        description=buku.description,
                        price=buku.price,
                        image_url=buku.image_url,
                        stock=buku.stock,
                    )
                )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return buku_pb2.BukuResponse()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(
                    update(Buku)
                    .where(Buku.id == request.id)
                    .values(
                        name=request.name,
                        description=request.description,
                        price=request.price,
                        image_url=request.image_url,
                        stock=request.stock,
                    )
                )

                conn.commit()

                return buku_pb2.BukuUpdateResponse(
                    buku=buku_pb2.Buku(
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
            return buku_pb2.BukuUpdateResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.execute(delete(Buku).where(Buku.id == request.id))

                conn.commit()

                return buku_pb2.BukuDeleteResponse(message="buku deleted successfully")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(traceback.format_exc())
            return buku_pb2.BukuDeleteResponse()


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buku_pb2_grpc.add_BukuServiceServicer_to_server(BukuService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Server started at port 50052")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    server()
