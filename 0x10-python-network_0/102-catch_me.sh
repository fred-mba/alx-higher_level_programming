#!/bin/bash
# Makes a request on the server to respond with a message containing You got me!
curl -sX "PUT" -d "user_id=98" --header "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
