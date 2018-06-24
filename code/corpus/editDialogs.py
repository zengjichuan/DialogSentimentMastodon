# prerequis:
# fichier toots.txt qui vient de downloadCorpus.py
# fichier dialogs.idx qui vient de buildDialogs.py

import io
import json

with io.open("dialogs.idx","r",encoding="utf-8") as f: lines=f.readlines()

allids=[]
for l in lines:
    i=l.find(':')
    ids=[int(s) for s in l[i+2:].strip().split()]
    allids+=ids
setids=set(allids)
assert len(setids)==len(allids)

toots = {}
with io.open("toots.txt","r",encoding="utf-8") as f:
    for l in f:
        res=json.loads(l)
        for t in res:
            if int(t['id']) in setids: toots[int(t['id'])]=t
print(len(toots))

def recurs(sons,cur,l):
    s=' '*l
    print(s+toots[cur]['account']['username']+": "+toots[cur]['content'])
    for son in sons[cur]:
        recurs(sons,son,l+2)

for l in lines:
    i=l.find(':')
    ids=[int(s) for s in l[i+2:].strip().split()]
    
    authors=[toots[i]['account']['username'] for i in ids]
    single =set(authors)
    if len(single)==1: continue

    root=int(l[0:i].strip().split()[-1])
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
 
