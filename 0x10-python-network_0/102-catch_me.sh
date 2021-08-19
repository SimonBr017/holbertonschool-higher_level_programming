#!/bin/bash
# 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" http://e87f0be5f87a.c3bcb5f8.hbtn-cod.io:5000/catch_me_3
