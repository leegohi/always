# -*- coding=utf-8 -*-

import subprocess
import requests
import os


def doc2txt(fobj):
    class ArgumentTypeException(Exception):
        pass
    try:
        if type(fobj) == str:
            f = open(fobj, "rb")
        elif hasattr(fobj, "read"):
            f = fobj
        else:
            raise ArgumentTypeException(
                "argument 'fobj' must be a file-like object or filename string.")
        f = fobj

        new_env = dict(os.environ)  # Copy current environment
        new_env['LANG'] = 'zh_CN.UTF-8'
        # 注意如果shell=True，命令和参数必须作为整体字符串。否则应为一个list
        sub_antiword = subprocess.Popen(["antiword", "-"], stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, stdin=subprocess.PIPE, close_fds=True, env=new_env)
        res, err = sub_antiword.communicate(f.read())
        return res
    finally:
        if "f" in locals():
            f.close()


if __name__ == "__main__":
    def download_doc():
        url = "http://zfxxgk.beijing.gov.cn/11K000/qtwj22/2018-04/10/e4a2e846d5594cc0beaadc82fec0b844/files/8cf80a79a2bb487a9d02dc5c005adeea.doc"
        headers = headers = {
            "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.181Safari/537.36",
            "Host": "zfxxgk.beijing.gov.cn",
            "Upgrade-Insecure-Requests": "1"
        }
        response = requests.get(url, headers=headers, stream=True)
        fobj = response.raw
        return doc2txt(fobj)
    print download_doc()
