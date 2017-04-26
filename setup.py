""" CNS Python based ORM Implementation (Common Schema Metadata)
"""
from setuptools import setup, find_packages


cfg = {
    'name'             : 'cns-orm-meta',
    'long_description' : __doc__,
    'version'          : '0.9.0',
    'packages'         : find_packages('src'),
    'package_dir'      : {'': 'src'},

    'namespace_packages': [
        'cns',
        'cns.orm'
    ],

    'install_requires': [
        'cns-orm-common >= 1.0.0'
    ],

    'dependency_links' : [],
    'zip_safe'         : False
}


if __name__ == '__main__':
    setup(**cfg)
