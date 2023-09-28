#!/bin/bash
# This script sends a PUT request to 0.0.0.0:5000/catch_me to get the desired response

# Send a PUT request with the specified data
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool" -o /dev/null -w "You got me!"
