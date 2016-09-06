# docker-site-tests
Docker site tests for code challenge.

### Setup
_this setup (particularly chromedriver installation) assumes a Mac/OSX system._
* Install requirements: `pip install -r requirements.txt`
* Set up chromedriver:
    * if you are using a mac: `./install_chromedriver.sh`
    * otherwise, download and extract the chromedriver binary into the `bin/` directory- it is available [here](http://chromedriver.storage.googleapis.com/index.html?path=2.23/)
    * basically, you need a path `./bin/chromedriver`

### Running tests:
`nosetests -v`

## Approach
I tested three core features using selenium from a user's point of view- no implementation, just validating ui messages. Further details are available in the test code.
