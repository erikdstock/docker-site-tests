#!/usr/bin/env bash
# Install chromedriver to the bin/ directory
echo "Installing chromedriver (for mac) to bin/..."
curl -O http://chromedriver.storage.googleapis.com/2.23/chromedriver_mac64.zip && \
	unzip chromedriver_mac64.zip -d bin/ && \
	rm chromedriver_mac64.zip && \
	echo "chromedriver installed"; exit 0


echo "something went wrong. please manually install chromedriver in the bin/ directory from http://chromedriver.storage.googleapis.com/index.html?path=2.23/."
exit 1
