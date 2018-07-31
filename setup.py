import os
import sys

from setuptools import setup

from .restcord.vars import __version__, __title__, __author__, __license__, __github__, __description__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = __version__
if not version:
    raise RuntimeError('version is not set')

with open('README.rst') as f:
    readme = f.read()

setup(name=__title__,
      author=__author__,
      version=version,
      packages=['restcord'],
      license=__license__,
      description=__description__,
      long_description=readme,
      url=__github__,
      include_package_data=True,
      install_requires=requirements,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ]
      )
