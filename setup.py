"""
Setup for configurate notexblock XBlock package.
"""

from __future__ import absolute_import

import os

from setuptools import setup


def package_data(pkg, roots):
    """
    Find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='notexblock',
    version='0.1.0',
    description='notexblock XBlock allows student make notes in the block notes',
    long_description=README,
    license='LICENSE',
    packages=[
        'notexblock',
    ],
    install_requires=[
        'XBlock',
    ],
    requires=[],
    entry_points={
        'xblock.v1': [
            'notexblock = notexblock:NoteXBlock',
        ]
    },
    package_data=package_data("notexblock", ["static", "public"]),
)
