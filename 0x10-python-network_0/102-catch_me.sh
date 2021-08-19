#!/bin/bash
# 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sX PUT -d "user_id=98" "$1" -H "Origin: HolbertonSchool"
