#encoding:utf-8
import sys
from urllib import  unquote,splitquery
import json
import subprocess
import os

def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    #这里的data为bytes类型，之后需要转成utf-8操作
    return data
def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    p.communicate()

txt=getClipboardData().decode("utf-8")
print(txt)

req=txt.split('\r')
print req
head={}
data={}
line1=req[0]
if "POST" in line1:
    line1=req[-1]
    if "&" in line1:
        param=unquote(line1.strip())
        print param
        data=dict(map(lambda i:i.split("=",1),param.split("&")))

else:
    qstr=splitquery(line1.split(" ")[1])[1]
    if qstr:
        param=unquote(qstr)
        data=dict(map(lambda i:i.split("=",1),param.split("&")))
    

txt=json.dumps(data,indent=1,ensure_ascii=False)+"\n"
for line in req[1:]:
    if  line.startswith("Cookie"):
        continue
    if  line.startswith("Content-Length"):
        continue 
    #if  line.startswith("Connection"):
    #    continue    
    if  not line.strip():
        break
    temp=line.strip().replace(" ","").split(":",1)
    print temp
    head[temp[0]]=temp[1]
    

txt+=json.dumps(head,indent=1,ensure_ascii=False)

#重新转成bytes型
data=txt.encode('utf8')
setClipboardData(data)

