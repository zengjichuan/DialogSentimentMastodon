# prerequis:
# fichier toots.txt qui vient de downloadCorpus.py
# fichier cleaned.txt qui vient de delDoublons.py
# fichier dialogs.idx qui vient de buildDialogs.py

import io
import json

with io.open("dialogs.idx","r",encoding="utf-8") as f: lines=f.readlines()

allids=[]
for l in lines:
    ids=[int(s) for s in l.strip().split()]
    allids+=ids
setids=set(allids)
assert len(setids)==len(allids)
print("nposts in dialogs",len(setids))

toots = {}
with io.open("toots.txt","r",encoding="utf-8") as f:
    for l in f:
        res=json.loads(l)
        for t in res:
            if int(t['id']) in setids: toots[int(t['id'])]=t
with io.open("cleaned.txt","r",encoding="utf-8") as f:
    for l in f:
        res=json.loads(l)
        for t in res:
            if int(t['id']) in setids: toots[int(t['id'])]=t
print("ntoots",len(toots))

def recurs(sons,cur,l):
    s='..'*l
    print(s+toots[cur]['account']['username']+": "+toots[cur]['content'])
    for son in sons[cur]:
        recurs(sons,son,l+2)

for l in lines:
    ids=[int(s) for s in l.strip().split()]
   
    # remove monologues 
    authors=[toots[i]['account']['username'] for i in ids]
    single =set(authors)
    if len(single)==1: continue

    # get the root
    root=ids[0]
    while True:
        if not 'in_reply_to_id' in toots[root]: break
        if toots[root]['in_reply_to_id']==None: break
        root=int(toots[root]['in_reply_to_id'])
    sons={}
    for id in ids: sons[id]=[]
    for id in ids:
        toot = toots[id]
        par = toot['in_reply_to_id']
        if not par==None:
            parid = int(par)
            sons[parid].append(id)
        else: assert id==root
    recurs(sons,root,0)
    print()
 
