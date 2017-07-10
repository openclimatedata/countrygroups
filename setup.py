"""
countrygroups
-------------

Install using ::

    pip install countrygroups

See README.md and repository for details:
    <https://github.com/openclimatedate/countrygroups>
"""

from setuptools import setup

import versioneer


cmdclass = versioneer.get_cmdclass()

setup(
    name='countrygroups',
    version=versioneer.get_version(),
    description='ISO-Codes of country groups, especially those related to the UNFCCC negotiation process',
    long_description=__doc__,
    url='https://github.com/openclimatedata/countrygroups',
    author='Robert Gieseke',
    author_email='robert.gieseke@pik-potsdam.de',
    license='BSD',
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
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
