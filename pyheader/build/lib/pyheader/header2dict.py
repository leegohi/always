#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urllib import unquote, splitquery
import json
import subprocess
import os
import traceback
from pyheader import WIN

if WIN:
    import win32clipboard as wc
    import win32con

def set_clip(data):
    if WIN:
        wc.OpenClipboard()
        try:
            wc.EmptyClipboard()
            copy_text = wc.SetClipboardText(data)
        except:
            traceback.print_exc()
        finally:
            wc.CloseClipboard()
        return
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data.encode(sys.stdout.encoding))
    p.stdin.close()
    p.communicate()


def get_clip():
    copy_text = None
    if WIN:
        wc.OpenClipboard()
        try:
            copy_text = str(wc.GetClipboardData(win32con.CF_UNICODETEXT))
        except:
            traceback.print_exc()
        finally:
            wc.CloseClipboard()
        copy_text= copy_text
    if not copy_text:
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        copy_text = p.stdout.read()
    return copy_text


def get_headers():
    copy_text = get_clip()
    print "RAW DATA:\n",copy_text
    req = copy_text.split('\r')
    if len(req) == 1:
        req = copy_text.split("\n")
    head = {}
    res=[]
    line1 = req[0]
    method="get"
    if "POST" in line1 or "PUT" in line1:
        method="post"
        lastline = req[-1]
        try:
            data=json.loads(lastline.strip())
            res.append("data="+json.dumps(data, indent=1, ensure_ascii=False))
        except:
            traceback.print_exc()
            if "&" in lastline or "=" in lastline:
                param = unquote(lastline.strip())
                data = dict(map(lambda i: i.split("=", 1), param.split("&")))
            else:
                data={}
            res.append("data="+json.dumps(data, indent=1, ensure_ascii=False))
    path,qstr = splitquery(line1.split(" ")[1])
    if qstr:
        param = unquote(qstr)
        data = dict(map(lambda i: i.split("=", 1), param.split("&")))
        res.append("params="+json.dumps(data, indent=1, ensure_ascii=False))
    for line in req[1:]:
        if line.startswith("Cookie"):
            continue
        if line.startswith("Content-Length"):
            continue
        if not line.strip():
            break
        temp = line.strip().replace(" ", "").split(":", 1)
        head[temp[0]] = temp[1]
    res.append("headers="+json.dumps(head, indent=1, ensure_ascii=False))
    if path.startswith("https://") or path.startswith("http://"):
        res.append('url="%s"'%path)
    else:
        res.append('url="%s"'%(head["Host"]+path))
    res.append("response=requests.%s(url,data=data,headers=headers,params=params)"%method)
    res_str="\n".join(res)
    decode_res=res_str.decode("utf-8")
    print decode_res
    #重新转成bytes型
    set_clip(decode_res)

def main():
    import warnings
    try:
        get_headers()
    except:
        traceback.print_exc()
        warnings.warn("""
        You should copy right HTTP form string from fiddler,chrome console or any other editor. 
        Example:        
            GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
            User-Agent: Fiddler/4.6.20173.38786 (.NET 4.0; WinNT 6.1.7601 SP1;)
            Pragma: no-cache
            Host: www.fiddler2.com
            Accept-Language: zh-CN
            Referer: http://fiddler2.com/client/4.6.20173.38786
            Accept-Encoding: gzip, deflate
            Connection: close
        """)
if __name__ == "__main__":
    main()
