#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
Usage: ./8-json_api.py <letter>
- The letter is send as the value of the variable 'q'.
- If no letter is provided, sends 'q="".
"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        r_dict = r.json()
        id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
