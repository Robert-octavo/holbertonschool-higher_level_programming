#!/bin/bash
# Write a Bash script that sends a request to a URL passed as an argument,
# and displays only the status code of the response.
# https://superuser.com/questions/272265/getting-curl-to-output-http-status-code
# https://curl.se/docs/manpage.html  look for --write-out section
# -o /dev/null To suppress response bodies, you can redirect output to /dev/null

curl -s -o /dev/null --write-out "%{http_code}" "$1"
