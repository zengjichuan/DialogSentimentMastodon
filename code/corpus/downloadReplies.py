#!/bin/python3

# start from the list of public status in the timeline, and get for each of them the ancestors and descendants

import requests
import io
import json

# put the instance needed here
inst='https://octodon.social/api/v1/'

# get the public statuses
allids = []
with io.open("toots.txt","r",encoding="utf-8") as f:
    for l in f:
        toots=json.loads(l)
        ids = [int(t['id']) for t in toots]
        allids+=ids

# download the descendants and ascendants
done=set()
todo = set(allids)
with io.open("replies.txt","a",encoding="utf8") as f:
    while len(todo)>0:
        id = todo.pop()
        done.add(id)
        print(str(id)+" done "+str(len(done))+" todo "+str(len(todo)))
        res = requests.get(inst+"/statuses/"+str(id)+"/context")
        ctxt = json.loads(res.text)
        if 'ancestors' in ctxt.keys():
            anc = ctxt['ancestors']
            for z in anc:
                zid = int(z['id'])
                if not zid in done:
                    toots = json.dumps(z)
                    f.write('['+toots+']\n') # keep it as an array for compatibility with toots.txt
                    # todo means that we have to look for its context; but writing the toot itself is already done
                    todo.add(zid)
        if 'descendants' in ctxt.keys():
            des = ctxt['descendants']
            for z in des:
                zid = int(z['id'])
                if not zid in done:
                    toots = json.dumps(z)
                    f.write('['+toots+']\n')
                    # todo means that we have to look for its context; but writing the toot itself is already done
                    todo.add(zid)

