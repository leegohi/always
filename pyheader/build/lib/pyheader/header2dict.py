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
            copy_text = wc.GetClipboardData(win32con.CF_UNICODETEXT)
        except:
            traceback.print_exc()
        finally:
            wc.CloseClipboard()

        return copy_text
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    copy_text = p.stdout.read().decode("utf-8")
    return copy_text


def get_headers():
    copy_text = get_clip()
    req = copy_text.split('\r')
    if len(req) == 1:
        req = copy_text.split("\n")
    print req
    head = {}
    res=[]
    line1 = req[0]
    if "POST" in line1 or "PUT" in line1:
        lastline = req[-1]
        try:
            data=json.loads(lastline.strip())
            res.append("POST DATA:")
            res.append(json.dumps(data, indent=1, ensure_ascii=False))
        except:
            traceback.print_exc()
            if "&" in lastline:
                param = unquote(lastline.strip())
                print param
                data = dict(map(lambda i: i.split("=", 1), param.split("&")))
        qstr = splitquery(line1.split(" ")[1])[1]
        if qstr:
            param = unquote(qstr)
            data = dict(map(lambda i: i.split("=", 1), param.split("&")))
            res.append("QUERY DATA:")
            res.append(json.dumps(data, indent=1, ensure_ascii=False))
    for line in req[1:]:
        if line.startswith("Cookie"):
            continue
        if line.startswith("Content-Length"):
            continue
        if not line.strip():
            break
        temp = line.strip().replace(" ", "").split(":", 1)
        print temp
        head[temp[0]] = temp[1]
    res.append("HEADERS:")
    res.append(json.dumps(head, indent=1, ensure_ascii=False))

    #重新转成bytes型
    set_clip("\n".join(res))

def main():
    get_headers()
if __name__ == "__main__":
    main()
