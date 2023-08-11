import re
from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# twine upload dist/*
def _read_long_description():
    try:
        with open("README.md") as fd:
            return fd.read()
    except Exception:
        return None
    


with open("ssi_fctrading/version.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
readme='TBD'


setup(
    name='ssi-fctrading',
    version=version,
    description='FastConnect TradingAPI client by Python',
    long_description=_read_long_description(),
    long_description_content_type='text/markdown',
    author='ducdv',
    author_email='ducdv@ssi.com.vn',
    license='MIT',
    platforms=['POSIX', 'Windows'],
    url='https://github.com/SSI-Securities-Corporation/python-fctrading',
    python_requires=">=3.7",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=False,
    install_requires=['pycryptodome',
                        'xmljson',
                        'requests>=2.18.4', 'websocket-client>=1.5.2',
                        'psutil'],
)


