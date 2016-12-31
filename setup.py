from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
  name='restypy',
  packages=find_packages(),
  version='0.5',
  description='A Pythonic Rest API client',
  long_description=long_description,
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
