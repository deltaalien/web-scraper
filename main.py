import requests

from ws.conf.ConfigLoader import ConfigLoader
import GlobalConstants
from ws.paginator.IterationPaginator import IterationPaginator


if __name__ == '__main__':
    config = ConfigLoader.load_from_file(GlobalConstants.PROJECT_ROOT+"/config/halo_oglasi.json")

    paginator = IterationPaginator(config)
    paginator.get_data()



