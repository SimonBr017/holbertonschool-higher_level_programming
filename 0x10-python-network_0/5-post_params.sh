#!/bin/bash
# sends a POST request
curl -sX POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
