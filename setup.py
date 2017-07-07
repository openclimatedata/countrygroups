"""
unfccc-groups
-------------

Install using ::

    pip install unfccc_groups

See README.md and repository for details:
    <https://github.com/openclimatedate/unfccc-groups>
"""

from setuptools import setup

import versioneer


cmdclass = versioneer.get_cmdclass()

setup(
    name='unfccc_groups',
    version=versioneer.get_version(),
    description='ISO-Codes of groups in or related to the UNFCCC process',
    long_description=__doc__,
    url='https://github.com/openclimatedata/unfccc-groups',
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
    keywords=['unfccc', 'climate change'],
    cmdclass=cmdclass,
    packages=['unfccc_group']
)
