import requests


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
        return getattr(requests, request_method, self)(request_path, *args, **kwargs)

    def __getattr__(self, item):
        if item != 'path' and item != 'url':
            if self.path is not None:
                new_path = self.path[:]
                new_path.append(item)
                return API(url=self.url, path=new_path)
            else:
                return API(url=self.url, path=[item])

if __name__ == '__main__':
    github = API('https://api.github.com')
    # Hit : https://api.github.com/users/simula67/events
    print github.users(url='simula67').events()

    # For HTTP methods other than GET, add a keyword argument 'method'. Rest of the arguments are passed to 'requests'
    httpbin = API('http://httpbin.org')
    print httpbin.post(method='post', data={'test': 'hi'})