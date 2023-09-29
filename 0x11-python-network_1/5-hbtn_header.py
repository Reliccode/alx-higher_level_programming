#!/usr/bin/python3
"""
script that sends request to URL and
displays value of a variable in response header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exception as e:
        print(f"An error occured : {e}")
