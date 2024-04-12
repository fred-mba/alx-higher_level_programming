#!/bin/bash
# Makes a request on the server to respond with a message containing You got me!
curl -s -X PUT -d "You got me!" -H "X-School-User-Id: 98" 0.0.0.0:5000/catch_me
