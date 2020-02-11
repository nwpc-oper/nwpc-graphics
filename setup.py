# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='nwpc-graphics',

    version='0.1.0',

    description='NWPC Graphics project.',
    long_description=__doc__,

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={
        '': ["*.ncl", "*.sh"],
    },

    zip_safe=False,

    install_requires=[
        'click',
        'pyyaml',
        "pytimeparse",
        "IPython",
        "loguru",
        "pillow"
    ],

    entry_points={
        "console_scripts": [
            "nwpc_graphics = nwpc_graphics._main:cli",
        ],
    },
)
