import json

from ws.conf.Config import Config
from ws.query.SearchQuery import SearchQuery


class ConfigLoader:
    @staticmethod
    def load_from_file(file_path):
        with open(file_path) as f:
            config_data = json.load(f)

        url = config_data["url"]
        pagination_format = config_data["pagination_format"]
        pagination_type = config_data["pagination_type"]
        stop = config_data["stop"]
        extraction = config_data["extraction"]
        enable_caching = config_data["enable_caching"]
        item = SearchQuery(**config_data["item"])
        data = config_data["data"]

        search_query_dict = {}
        for key, value in data.items():
            query = value["query"]
            data_attribute = value["data_attribute"]
            search_query_dict[key] = SearchQuery(query, data_attribute)

        return Config(url, pagination_format, pagination_type, stop, extraction, enable_caching, item,
                      search_query_dict)


def main():
    config = ConfigLoader.load_from_file("../../config/halo_oglasi.json")
    print(config)


if __name__ == "__main__":
    main()
