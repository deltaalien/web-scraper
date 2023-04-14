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
        item = SearchQuery(**config_data["item"])
        data = config_data["data"]

        search_query_dict = {}
        for key, value in data.items():
            element = value["element"]
            data_attribute = value["data_attribute"]
            attributes = value["attributes"]
            search_query_dict[key] = SearchQuery(element, data_attribute, attributes)

        return Config(url, pagination_format, pagination_type, stop, extraction, item, search_query_dict)


def main():
    config = ConfigLoader.load_from_file("../../config/halo_oglasi.json")
    print(config)


if __name__ == "__main__":
    main()
