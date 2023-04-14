import requests

from ws.conf.ConfigLoader import ConfigLoader
import GlobalConstants
from ws.query.QueryExecutor import QueryExecutor

if __name__ == '__main__':
    config = ConfigLoader.load_from_file(GlobalConstants.PROJECT_ROOT+"/config/halo_oglasi.json")

    query = config.item

    print(query.attributes)

    response = requests.get(config.url)
    result = QueryExecutor.execute(response, config.item)

    for i in result:
        print(i)
        print("\n")

