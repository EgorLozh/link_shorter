import punq

from functools import lru_cache

from app.sql_app.base import AsyncAbstractRedirectLinkRepo



@lru_cache(1)
def get_container() -> punq.Container:
    return _init_container()


def _init_container() -> punq.Container:
    container = punq.Container()

    from app.sql_app.repos import RedirectLinkRepo
    container.register(AsyncAbstractRedirectLinkRepo, RedirectLinkRepo)

    return container
