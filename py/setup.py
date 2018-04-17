"""
countrygroups
-------------

Install using ::

    pip install countrygroups

See README.md and repository for details:
    https://github.com/openclimatedate/countrygroups
"""

from setuptools import setup
import os

import versioneer

path = os.path.abspath(os.path.dirname(__file__))

description = (
    'Country groups as lists of ISO codes, especially those '
    'related to the UNFCCC climate policy process'
)

with open(os.path.join(path, '../README.md'), "r") as f:
    readme = f.read()

cmdclass = versioneer.get_cmdclass()

setup(
    name='countrygroups',
    version=versioneer.get_version(),
    description=description,
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/openclimatedata/countrygroups',
    author='Robert Gieseke',
    author_email='robert.gieseke@pik-potsdam.de',
    license='CC0',
    install_requires=['shortcountrynames'],
    platforms='any',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['country code', 'country groups', 'unfccc', 'climate change'],
    cmdclass=cmdclass,
    packages=['countrygroups']
)
