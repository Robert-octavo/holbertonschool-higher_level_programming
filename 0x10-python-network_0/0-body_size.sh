#!/bin/bash
# Bash script that takes in a URL, sends a request
# to that URL, and displays the size of the body of
# the response
# https://stackoverflow.com/questions/4497759/how-to-get-remote-file-size-from-a-shell-script
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
