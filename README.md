# docker-site-tests
Docker site tests for Flashpoint

## Running tests
### Setup

* Install requirements: `pip install -r requirements.txt`
* Set up chromedriver:
    * if you are using a mac: `./install_chromedriver.sh`
    * otherwise, download and extract the chromedriver binary into the `bin/` directory- it is available [here](http://chromedriver.storage.googleapis.com/index.html?path=2.23/)

### run tests: 
*`nosetests`

## Approach
I tested three core features using selenium from a user's point of view- no implementation, just validating ui messages. further details are available in the test code.