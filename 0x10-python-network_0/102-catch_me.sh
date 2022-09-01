#!/bin/bash
# Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that
# causes the server to respond with a message containing You got me!,
# in the body of the response.
# https://reqbin.com/req/c-taimahsa/curl-cors-request
URL="0.0.0.0:5000/catch_me"
# curl -s -X POST --header 'Host:' "$URL" answer: methon not allowed change for PUT
# curl -s -X PUT --header 'Host:' "$URL" answer: You should be redirected automatically to target
# curl -sL -X PUT --header 'Host:' "$URL" add location to redirect / answer: You are not user_id = 98
# curl -sL -X PUT --header 'Host:' --data "user_id=98" "$URL" answer: You are not coming from HolbertonSchool
# change the Host: to Origin: HolbertonSchool
curl -sL -X PUT --header 'Origin: HolbertonSchool' --data "user_id=98" "$URL"
