#encoding:utf-8
import requests
def set_requests2selenium(requests_cookie,driver,domain):
    cookie_dic=requests.utils.dict_from_cookiejar(requests_cookie)
    driver_cookies=map(lambda i:{"name":i[0],"value":i[1],"domain":domain,'path': '/','expires': None},cookie_dic.items())
    for cookie in driver_cookies:
        driver.add_cookie(cookie)
