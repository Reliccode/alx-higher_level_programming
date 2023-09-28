#!/bin/bash
# This script sends a PUT request to 0.0.0.0:5000/catch_me to get the desired response

# Send a PUT request with the specified data and headers
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me | grep "You got me!" --quiet && echo "You got me!"
