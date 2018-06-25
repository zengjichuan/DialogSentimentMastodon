#!/bin/python3

# this script should be run with a "script" command to save the output into a file

import requests
import io
import json

# put the instance needed here
inst='https://octodon.social/api/v1/timelines/public?local=1'

with io.open("toots.txt","a",encoding="utf8") as f:
    while True:
        res = requests.get(inst)
        toots = res.text
        f.write(toots+'\n')
        headers = res.headers
        links = headers['Link']
        suiv=links.split()[0].replace('<',' ').replace('>',' ').replace(';',' ').strip()
        print(suiv)
        if not suiv.startswith("https") or suiv==inst: break
        inst=suiv

# reload
# with io.open("toots.txt","r",encoding="utf-8") as f:
#     for l in f:
#         res=json.loads(l)
#         for t in res: print(t['content'])

# this script only downloads the posts in the public local timeline: so there is no dialog in there yet !
# look at downloadReplies.py next to get the dialogs

