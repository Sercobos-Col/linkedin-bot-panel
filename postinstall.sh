#!/bin/bash
apt-get update -y
apt-get install -y wget gnupg2 curl unzip
wget -q -O - https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > /tmp/chrome.deb
dpkg -i /tmp/chrome.deb
apt-get -y install -f
playwright install
