#!/bin/bash
# Write a Bash script that takes in a URL, sends a POST request to
# the passed URL, and displays the body of the response
# https://akrabat.com/view-header-and-body-with-curl/
# https://curl.se/docs/manpage.html  look for --data section

curl -s -X POST --data "email=test@gmail.com" --data "subject=I will always be here for PLD" "$1"
