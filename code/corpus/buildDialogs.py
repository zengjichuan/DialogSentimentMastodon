#!/bin/python3

import io
import json

fich = "toots.txt"

def show():
    # reload and show toots
    with io.open(fich,"r",encoding="utf-8") as f:
        for i in range(1):
            l=f.readline()
            res=json.loads(l)
            for t in res:
                # parent = t['in_reply_to_id']
                # print(t['id']+" "+str(parent))
                print(t['content'])

dialognodes=[]

class DialNode:
    def __init__(self,i):
        # utilise lorsqu'on cree un nouveau parent
        self.id=i
        self.sons=[]
        self.dad=None
        self.idx=len(dialognodes)
        dialognodes.append(self)

def builddialogs():
    dialroots=[]
    for d in dialognodes:
        if d.dad==None: dialroots.append(d.idx)
    return dialroots

def checkDups():
    ids=[]
    for d in dialognodes: ids.append(d.id)
    z=set(ids)
    assert len(z)==len(ids)
    print("check dups ok")

def recurs(lnodes,curidx):
    node=dialognodes[curidx]
    lnodes.append(node.id)
    for filsidx in node.sons:
        recurs(lnodes,filsidx)

def savedialogs():
    roots=builddialogs()
    with io.open("dialogs.idx","w",encoding="utf-8") as f:
        for r in roots:
            nodesindial=[]
            recurs(nodesindial,r)
            f.write("root "+str(dialognodes[r].id)+" : "+' '.join([str(x) for x in nodesindial])+'\n')

def addLink(i,p):
    cur=None
    for dial in dialognodes:
        if dial.id==i:
            # node deja enregistre, probablement car il est le parent d'un autre node
            cur=dial
            break
    if cur==None: cur=DialNode(i)
    # ici, cur contient le noeud i et est deja dans la liste dialogs
    par=None
    for dial in dialognodes:
        if dial.id==p:
            # le parent est deja dans la liste
            par=dial
            break
    if par==None: par=DialNode(p)
    # ici, par contient le parent et est deja dans la liste dialogs
    par.sons.append(cur.idx)
    assert cur.dad==None
    cur.dad=par.idx

def dialogs():
    allids,par=[],[]
    with io.open(fich,"r",encoding="utf-8") as f:
        for l in f:
            res=json.loads(l)
            for t in res:
                parentstr = t['in_reply_to_id']
                if parentstr==None: parent=None
                else: parent = int(parentstr)
                curid = int(t['id'])
                allids.append(curid)
                par.append(parent)
    print("ids %d %d" % (min(allids),max(allids)))
    np,npin=0,0
    for i in range(len(allids)):
        if i%1000==0: print("step %d %d" % (i,len(allids)))
        p=par[i]
        if not p==None:
            np+=1
            if p in allids:
                npin+=1
                addLink(allids[i],p)
    print("ntweets %d nparents %d nparentsin %d" % (len(allids),np,npin))
    checkDups()

dialogs()
savedialogs()

