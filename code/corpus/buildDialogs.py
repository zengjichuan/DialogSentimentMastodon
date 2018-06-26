#!/bin/python3

import io
import json

fich = ["cleaned.txt","toots.txt"]

id2clust = {}
id2parent = {}

# pass 1: initialize every post to its own cluster
for ff in fich:
    with io.open(ff,"r",encoding="utf-8") as f:
        for l in f:
            res=json.loads(l)
            for t in res:
                parentstr = t['in_reply_to_id']
                if not parentstr==None:
                    curid = int(t['id'])
                    id2clust[curid]=curid
                    id2parent[curid]=int(parentstr)

# pass 2: merge clusters
while True:
    modif=0
    for i in id2clust.keys():
        parentid = id2parent[i]
        if parentid in id2clust:
            if not id2clust[i]==id2clust[parentid]:
                id2clust[i]=id2clust[parentid]
                modif+=1
        else: id2clust[i]=parentid
    print(modif)
    if modif==0: break

# group posts
clust2posts = {}
for i in id2clust.keys():
    clust=id2clust[i]
    if not clust in clust2posts:
        posts=set()
        clust2posts[clust]=posts
    else: posts=clust2posts[clust]
    posts.add(i)
    posts.add(id2parent[i])

with io.open("dialogs.idx","w",encoding="utf-8") as f:
    for posts in clust2posts.values():
        f.write(' '.join([str(x) for x in list(posts)])+'\n')

