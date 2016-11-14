import json
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('user', 'user')

# List of lists
r = requests.get(
    'http://127.0.0.1:8000/todo/todolists',
    auth=auth)

# A list
r = requests.get(
    'http://127.0.0.1:8000/todo/todolists/1',
    auth=auth)
#print r.json

# A task
x = requests.get(
    'http://127.0.0.1:8000/todo/tasks/2',
    auth=auth)
import pdb; pdb.set_trace()
print x.json()

"""
# Create a list
x = requests.post(
    'http://127.0.0.1:8000/todo/todolists/',
    data={'label': 'Test'},
    auth=auth)
"""
