#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and displays the response

# Send a POST request with a custom header to trigger the server response
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
