#!/bin/bash
# Write a Bash script that takes in a URL and displays
# all HTTP methods the server will accept.
# https://stackoverflow.com/questions/42549146/how-do-you-find-the-list-of-all-the-supported-http-methods-by-a-webserver
# https://linuxhint.com/bash-cut-command-examples/
curl -sI -X OPTIONS "$1" | grep -i Allow: | cut -d " " -f 2-
