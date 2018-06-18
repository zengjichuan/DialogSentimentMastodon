#!/bin/python3

import io
import json

# reload and show toots
with io.open("toots.txt","r",encoding="utf-8") as f:
    for l in f:
        res=json.loads(l)
        for t in res:
            # parent = t['in_reply_to_id']
            # print(t['id']+" "+str(parent))
            print(t['content'])


