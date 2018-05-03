# always
目录里主要封装了一些自己常用的方法
## 1. doc2txt
** 本函数主要目的是方便在写爬虫的时候遇到word附件，下载后直接提取出文本文件。

注意：需要安装antiword

mac下: brew install antiword
## 2. find_path_in_json
** 本函数主要目的是方便在遇到大json时候，查找value是否存在于json中，返回其在json里的路径。

## 3. header2dict
** 本模块主要是方便写爬虫的时候，将fiddler里的raw也就是原始请求，转换成python字典（目前只支持mac）。

比如fiddler里抓到的原始请求是：

```http
GET https://test.com/address/address?callback=jQuery1102092&v=0.43041341799949273&areaid=0&_=1523927277183 HTTP/1.1
Host:test.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept: */*
Referer: https://myi.vip.com/address.html?ff=103|2|2|4
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: cps=adp%3Auopxvvef%3A%3A%3A%3A; vip_first_visitor=1;
```

直接copy原始请求（command+c）

执行

python header2dict.py

然后随便找个文本编辑器粘贴（command+v）

```json
{
 "callback": "jQuery110209262651116238236_1523927277176", 
 "areaid": "0", 
 "_": "1523927277183", 
 "v": "0.43041341799949273"
}
```

```json
{
 "Accept-Language": "zh-CN,zh;q=0.9", 
 "Accept-Encoding": "gzip,deflate,br", 
 "Connection": "keep-alive", 
 "Accept": "*/*", 
 "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.181Safari/537.36", 
 "Host": "test.com", 
 "Referer": "https://myi.vip.com/address.html?ff=103|2|2|4"
}
```

请求参数和header都出来了

## 4. download_with_progress
** 本模块主要是方便使用requests下载一些比较大的文件的时候。加个友好的进度条如下：

fetch baidu python img  [####################################]  100%
