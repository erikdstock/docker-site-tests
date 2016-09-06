# docker-site-tests
Docker site tests for Flashpoint

## Running tests
* If you use it, activate virtualenv: `source venv/bin/activate`
### Setup
* install requirements: `pip install -r requirements.txt`
* Setup chromedriver:
    * if you are using a mac: `./install_chromedriver.sh`
    * otherwise, download and extract the chromedriver binary into the `bin/` directory- it is available [here](http://chromedriver.storage.googleapis.com/index.html?path=2.23/)
### run tests: 
*`nosetests`
* When finished: `deactivate` venv
