# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='astroimages_api',
    version='1.0.0',
    description='AstroImages API',
    long_description=readme,
    author='Rodrigo de Souza',
    author_email='rsouza01@gmail.com',
    url='https://github.com/AstroImages/astroimages-api',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
