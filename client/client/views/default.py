from pyramid.view import view_config, view_defaults
from client.buku_client import BukuClient
import traceback
import client.buku_pb2 as buku_pb2


@view_config(route_name="bukus", renderer="json")
def bukus_view(request):
    try:
        client = BukuClient()
        bukus = client.get_bukus()
        return bukus
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="bukus", renderer="json", request_method="POST")
def create_buku_view(request):
    try:
        if (
            request.json_body is None
            or "name" not in request.json_body
            or "description" not in request.json_body
            or "price" not in request.json_body
            or "image_url" not in request.json_body
            or "stock" not in request.json_body
        ):
            request.response.status = 400
            return dict(
                status="error",
                message="Bad request",
            )

        client = BukuClient()
        buku = client.create_buku(
            buku=buku_pb2.Buku(
                name=request.json_body["name"],
                description=request.json_body["description"],
                price=request.json_body["price"],
                image_url=request.json_body["image_url"],
                stock=request.json_body["stock"],
            )
        )

        if "error" in buku:
            request.response.status = 400
            return dict(
                status="error",
                message=buku["error"]["message"],
            )

        return buku
    except Exception as e:
        print(traceback.format_exc())
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="buku", renderer="json", request_method="PUT")
def update_buku_view(request):
    try:
        if (
            request.json_body is None
            or "name" not in request.json_body
            or "description" not in request.json_body
            or "price" not in request.json_body
            or "image_url" not in request.json_body
            or "stock" not in request.json_body
        ):
            request.response.status = 400
            return dict(
                status="error",
                message="Bad request",
            )

        client = BukuClient()
        buku = client.update_buku(
            buku=buku_pb2.Buku(
                id=int(request.matchdict["id"]),
                name=request.json_body["name"],
                description=request.json_body["description"],
                price=request.json_body["price"],
                image_url=request.json_body["image_url"],
                stock=request.json_body["stock"],
            )
        )

        if "error" in buku:
            request.response.status = 400
            return dict(
                status="error",
                message=buku["error"]["message"],
            )

        return buku
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="buku", renderer="json", request_method="DELETE")
def delete_buku_view(request):
    try:
        client = BukuClient()
        buku = client.delete_buku(int(request.matchdict["id"]))

        if "error" in buku:
            request.response.status = 404
            return dict(
                status="error",
                message=buku["error"]["message"],
            )

        return buku
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="buku", renderer="json")
def buku_view(request):
    try:
        client = BukuClient()
        buku = client.get_buku(int(request.matchdict["id"]))

        if "error" in buku:
            request.response.status = 404
            return dict(
                status="error",
                message=buku["error"]["message"],
            )

        return buku
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )
