#!/usr/bin/env python
from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# twine upload dist/*

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
readme='TBD'


setup(
    name='ssi_fctrading',
    version='2.3.0',
    description='FastConnect TradingAPI client by Python',
    long_description=readme,
    author='ducdv',
    author_email='ducdv@ssi.com.vn',
    license='Property',
    platforms=['POSIX', 'Windows'],
    url='ssi.com.vn',
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 1 - Beta',
        'License :: OSI Approved :: Property License',
        'Environment :: Console',
        'Operating System :: POSIX Windows',
        'Programming Language :: Python :: 3.7'],
    # entry_points={'console_scripts': [
    #     'cython_npm = cython_npm:main',
    # ]},
    packages=find_packages(exclude=('test*','testpandoc*' )),
    include_package_data=False,
    install_requires=['pycryptodome',
                        'xmljson',
                        'requests',
                        'signalr-client',
                        'pyjwt'],
)


