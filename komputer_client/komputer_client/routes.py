def includeme(config):
    config.add_route("komputers", "/komputer")
    config.add_route("komputer", "/komputer/{id}")
