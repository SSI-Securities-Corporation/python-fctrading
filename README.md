# Build package
- Run `setup.bat` to build sdist

# Install ssi_fctrading

- Install from PyPi:  `pip install ssi_fctrading`
- Install from build:
    ```
    git clone https://github.com/SSI-Securities-Corporation/python-fctrading.git
    cd python-fctrading
    ./setup.bat
    pip install ssi_fctrading --force-reinstall --find-links dist/
    ```
# Run Example

- Install requirement: `pip install -r examples/requirements.txt`
- Config your key and PIN in file `examples/fc_config.py`
- Run `example_api.bat` to start example and open browser at [Swagger](http://127.0.0.1:8000/docs) to test
- Run `example_stream.bat` to start streaming