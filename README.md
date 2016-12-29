Restypy
=======

Pythonic REST client
The code interacting with the remote API reads just like standard Python!

Restypy uses the awesome 'requests' library under the hood

NOTE
====

Since REST APIs may contain URLs that may be invalid method names in Python, you will have to use the url='1nvalidpath' workaround to build the path.
This approach is shown in the following example.

Examples
========

    from restypy import API
    api = API('https://api.github.com')
    print api.users(url='simula67').events()

    # For HTTP methods other than GET, add a keyword argument 'method'. Rest of the arguments are passed to 'requests'
    api = API('http://httpbin.org')
    print api.post(method='post', data={'test': 'hi'})