# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-project-admin",
    version = "0.1",
    url = 'https://github.com/ONGEI/django-project-admin',
    license = 'GPL V.3',
    description = "Aplicación escrita en django que permite darle un seguimiento a un proyecto, nada que no sea conocido, asignación de tareas por ticket, wiki, archivos, etc.",
    long_description = read('README.rst'),

    author = 'O.N.G.E.I',
    author_email = 'ONGEI@pcm.gob.pe',

    packages = find_packages(),
    
    install_requires = ['setuptools',],

    classifiers = [
        'Development Status :: 4 - Dev',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
