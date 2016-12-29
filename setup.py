from setuptools import setup, find_packages
setup(
  name='restypy',
  packages=find_packages(),
  version='0.4',
  description='A Pythonic Rest API client',
  install_requires=[
        'requests'
  ],
  author='Joji Antony',
  author_email='simula67@gmail.com',
  url='https://github.com/simula67/restypy',
  download_url='https://github.com/simula67/restypy/tarball/master',
  keywords=['rest', 'pythonic', 'client'],
  classifiers=[],
)
