from pyramid.config import Configurator


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.include(".cors")
        config.add_cors_preflight_handler()
        config.include(".routes")
        config.scan()
    return config.make_wsgi_app()
