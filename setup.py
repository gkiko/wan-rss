from setuptools import setup, find_packages
import sys
import os

version = '0.0'

setup(name='wan-rss',
      version=version,
      description="convert html pagee to rss",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='rest atom rss flask requests',
      author='Giorgi Kikolashvili',
      author_email='gkiko10@freeuni.edu.ge',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'flask',
          'requests',
          'beautifulsoup4',
          'lxml',
          'feedgen',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
