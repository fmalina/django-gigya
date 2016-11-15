# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
import gigya as app

setup(
    name="Django GIGYA",
    version=app.__version__,
    description='Integrate GIGYA Customer identity and access management into Django projects using Django auth.',
    long_description=open('README.rst').read(),
    license='BSD License',
    platforms=['OS Independent'],
    keywords='authentication, auth, access, django, GIGYA, customer, identity',
    author='fmalina',
    author_email='fmalina@gmail.com',
    url="https://github.com/fmalina/django-gigya",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().split(),
)
