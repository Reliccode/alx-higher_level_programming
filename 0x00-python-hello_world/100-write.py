#!/usr/bin/python3
import sys
def print_message(message):
    sys.stderr.write(message + '\n')

message = "and that piece of art is useful - Dora Korpar, 2015-10-19"

print_message(message)
sys.exit(1)
