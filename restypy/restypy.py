import json
import requests
import yaml


class APIResponse:
    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return self.response.text

    @property
    def json(self):
        return json.loads(self.response.text)

    @property
    def yaml(self):
        return yaml.load(self.response.text)


class API:
    def __init__(self, url=None, path=None):
        if url is not None:
            self.url = url
        if path is not None:
            self.path = path

    def __call__(self, *args, **kwargs):
        if 'url' in kwargs:
            new_path = self.path[:]
            new_path.append(kwargs.get('url'))
            return API(url=self.url, path=new_path)
        request_path = self.url + '/' + '/'.join(self.path)
        request_method = kwargs.pop('method', 'get')
        r = getattr(requests, request_method, self)(request_path, *args, **kwargs)
        return APIResponse(r)

    def __getattr__(self, item):
        if item != 'path' and item != 'url':
            if self.path is not None:
                new_path = self.path[:]
                new_path.append(item)
                return API(url=self.url, path=new_path)
            else:
                return API(url=self.url, path=[item])

if __name__ == '__main__':
    api = API('http://httpbin.org')
    print api.post(method='post', data={'test': 'hi'})