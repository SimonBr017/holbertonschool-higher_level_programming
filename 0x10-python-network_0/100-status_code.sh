#!/bin/bash
# send a POST request with the content of a file
curl -s -o /dev/null -w "%{http_code}" "$1"
