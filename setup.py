from setuptools import setup, find_packages
setup(
  name = 'restypy',
  packages = find_packages(), # this must be the same as the name above
  version = '0.1',
  description = 'A Pythonic Rest API client',
  install_requires=[
        'PyYAML',
        'requests'
  ],
  author = 'Joji Antony',
  author_email = 'simula67@gmail.com',
  url = 'https://github.com/simula67/restypy', # use the URL to the github repo
  download_url = 'https://github.com/simula67/restypy/tarball/master', # I'll explain this in a second
  keywords = ['rest', 'pythonic', 'client'], # arbitrary keywords
  classifiers = [],
)
