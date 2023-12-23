from pyramid.view import view_config, view_defaults
from komputer_client.iniclient import KomputerClient
import traceback
import komputer_client.komputer_pb2 as komputer_pb2


@view_config(route_name="komputers", renderer="json")
def komputers_view(request):
    try:
        client = KomputerClient()
        komputers = client.get_komputers()

        return komputers
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="komputers", renderer="json", request_method="POST")
def create_komputer_view(request):
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

        client = KomputerClient()
        komputer = client.create_komputer(
            komputer=komputer_pb2.Komputer(
                name=request.json_body["name"],
                description=request.json_body["description"],
                price=request.json_body["price"],
                image_url=request.json_body["image_url"],
                stock=request.json_body["stock"],
            )
        )

        if "error" in komputer:
            request.response.status = 400
            return dict(
                status="error",
                message=komputer["error"]["message"],
            )

        return komputer
    except Exception as e:
        print(traceback.format_exc())
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="komputer", renderer="json", request_method="PUT")
def update_komputer_view(request):
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

        client = KomputerClient()
        komputer = client.update_komputer(
            komputer=komputer_pb2.Komputer(
                id=int(request.matchdict["id"]),
                name=request.json_body["name"],
                description=request.json_body["description"],
                price=request.json_body["price"],
                image_url=request.json_body["image_url"],
                stock=request.json_body["stock"],
            )
        )

        if "error" in komputer:
            request.response.status = 400
            return dict(
                status="error",
                message=komputer["error"]["message"],
            )

        return komputer
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="komputer", renderer="json", request_method="DELETE")
def delete_komputer_view(request):
    try:
        client = KomputerClient()
        komputer = client.delete_komputer(int(request.matchdict["id"]))

        if "error" in komputer:
            request.response.status = 404
            return dict(
                status="error",
                message=komputer["error"]["message"],
            )

        return komputer
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )


@view_config(route_name="komputer", renderer="json")
def komputer_view(request):
    try:
        client = KomputerClient()
        komputer = client.get_komputer(int(request.matchdict["id"]))

        if "error" in komputer:
            request.response.status = 404
            return dict(
                status="error",
                message=komputer["error"]["message"],
            )

        return komputer
    except Exception as e:
        request.response.status = 500
        return dict(
            status="error",
            message=str(e),
        )
