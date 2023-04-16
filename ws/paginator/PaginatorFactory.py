from typing import Optional

from ws.conf.Config import Config
from ws.paginator.AbstractPaginator import AbstractPaginator
from ws.paginator.IterationPaginator import IterationPaginator


class PaginatorFactory:

    @staticmethod
    def get(paginator: str, config: Config) -> Optional[AbstractPaginator]:
        if not paginator:
            return None

        if "ITERATION_STANDARD" == paginator:
            return IterationPaginator(config)

        return None
