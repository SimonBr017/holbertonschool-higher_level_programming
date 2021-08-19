#!/bin/bash
#takes in a URL, sends a request URL, displays size of body
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
