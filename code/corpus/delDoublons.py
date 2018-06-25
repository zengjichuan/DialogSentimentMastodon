import io
import json

allids=[]
with io.open("replies.txt","r",encoding="utf-8") as f:
    with io.open("cleaned.txt","w",encoding="utf-8") as g:
        for l in f:
            res=json.loads(l)
            # ca marche parce que je sais qu'il n'y a qu'un seul toot par ligne !
            for t in res:
                ii=int(t['id'])
                if ii in allids:
                    print(ii)
                else:
                    l=l.strip()
                    g.write(l+'\n')
                    allids.append(ii)

