import requests


class RestClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, url, params=None):
        return self._send_request('GET', url, params=params)

    def post(self, url, data=None, json=None):
        return self._send_request('POST', url, data=data, json=json)

    def put(self, url, data=None, json=None):
        return self._send_request('PUT', url, data=data, json=json)

    def delete(self, url):
        return self._send_request('DELETE', url)

    def _send_request(self, method, url, **kwargs):
        full_url = self.base_url + url
        headers = self.headers.copy()
        headers.update(kwargs.pop('headers', {}))
        response = requests.request(method, full_url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()
