import requests as req
import sys
import re
import time

if len(sys.argv) == 2: 
    server = sys.argv[1]
else:
    server = ''

while True:
    resp = req.get(server)
    content = resp.text
    stripped = re.sub('<[^<]+?>', '', content)
    print(stripped)
    time.sleep(5)
