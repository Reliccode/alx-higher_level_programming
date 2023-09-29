#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib."""

import urllib.request

def fetch_and_display_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status
    and displays info.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print('Body response:')
            print('\t- type: {}'.format(type(html)))
            print('\t- content: {}'.format(html))
            print('\t- utf8 content: {}'.format(html.decode('utf-8')))
    except urllib.error.URLError as e:
        print('Error:', e)

if __name__ == '__main__':
    fetch_and_display_status()
