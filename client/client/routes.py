def includeme(config):
    config.add_route("home", "/")
    config.add_route("bukus", "/buku")
    config.add_route("buku", "/buku/{id}")
