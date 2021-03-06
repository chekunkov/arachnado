#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='arachnado',
    version='0.1',
    url='https://github.com/TeamHG-Memex/arachnado',
    description='Scrapy-based Web Crawler with an UI',
    long_description=open('README.rst').read(),
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'arachnado': [
            "settings/*.conf",
            "templates/*.html",
            "static/css/*.css",
            
            "static/build/*.css",
            "static/build/*.js",

            "static/js/*.jsx",
            "static/js/*.js",
            "static/js/components/*.jsx",
            "static/js/components/*.js",
            "static/js/pages/*.jsx",
            "static/js/pages/*.js",
            "static/js/stores/*.jsx",
            "static/js/stores/*.js",
            "static/js/utils/*.jsx",
            "static/js/utils/*.js",
        ]
    },

    zip_safe=False,
    entry_points={
        'console_scripts': ['arachnado = arachnado.__main__:run']
    },
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'scrapy >= 1.0.0',
        'Twisted >= 12',
        'psutil >= 2.2',
        'tornado >= 4.2',
        'docopt >= 0.6',
        'service_identity',
    ],
)
