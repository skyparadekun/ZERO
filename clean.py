import json
fw = open("info.txt","r",encoding="utf-8")
indexes=['id','name','url','pic','rate','director','composer','actor','flag','district','language','showtime','length','othername','text']
cnt=1
for i in fw:
    info=i.split('^')
    new_dict=dict(zip(indexes,info))
    categories = info[8].split('/')
    for category in categories:
        s="data/"+category+".json"
        f=open(s,"at",encoding="utf-8")
        json.dump(new_dict,f)
        f.close()
fw.close()