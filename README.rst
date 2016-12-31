Restypy
=======

Pythonic REST client

The code interacting with the remote API reads just like standard Python!

Restypy uses the awesome 'requests' library under the hood

NOTE
====

Since REST APIs may contain URLs that may be invalid method names in Python, you will have to use the path='1nvalidpath' workaround to build the path.
This approach is shown in the following example.

Examples
========

.. code-block:: python

    from restypy import API
    github = API('https://api.github.com')
    # GET : https://api.github.com/users/simula67/events
    response = github.users(path='simula67').events()
    # Response is a simple 'requests' response
    print response.json()
    # For HTTP methods other than GET, add a keyword argument 'method'. Rest of the arguments are passed to 'requests'
    httpbin = API('http://httpbin.org')
    print httpbin.post(method='post', data={'test': 'hi'}).text
