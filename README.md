Restypy
=======

Pythonic rest client

Examples
========

    from restypy import API
    api = API('https://api.github.com')
    print api.users(url='simula67').events()
