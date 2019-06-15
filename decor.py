#encoding:utf-8
from __future__ import print_function
import traceback
import functools
def retry(times=3):
    """重试函数
    
    Keyword Arguments:
        times {int} -- 重试次数 (default: {3})
    """
    def wrapfunc(func):
        @functools.wraps(func)
        def wrapps(*args,**kwargs):
            i=0
            while i<times:
                try:
                    return func(*args,**kwargs)
                    break
                except:
                    traceback.print_exc()
                    print("timeout,retry %s times"%i)
                    i+=1
        return wrapps
    return wrapfunc