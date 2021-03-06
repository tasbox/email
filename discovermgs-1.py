# -*- coding: utf8 -*-
import os
import time
import json
from glob import glob
import multiprocessing

import requests
from loguru import logger


def get_proxyies() -> dict:
    """"""
    url = 'http://api1.ydaili.cn/tools/BUnlimitedApi.ashx?key=7705CE9CFCA646BD1CE64932B765CE35&action=BUnlimited&qty=1&orderNum=32887&isp=&format=txt'
    response = requests.get(url, timeout=15)
    text = response.text.splitlines()[0]
    proxies = {
        'http': 'http://%s' % text,
        'https': 'http://%s' % text
    }
    return proxies


class Discovermgs(object):
    """"""

    @staticmethod
    def get_cookie(proxies=None):
        """"""
        url = "https://discovermgs.avature.net/WorkMyWay?jobId=3465"
        payload = {}
        headers = {
            'authority': 'discovermgs.avature.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
        return response.cookies

    @staticmethod
    def send_email(cookies, proxies=None):
        """"""
        url = "https://discovermgs.avature.net/WorkMyWay/SendToAFriend?jobId=3465"

        payload = 'id=3465&send=&jobview=jobDetail&yourName=%E6%88%98%E7%A5%9E&yourEmail=3124541%40qq.com&friendEmail=25008793%40qq.com&subject=%E5%9C%A8%E7%BA%BF%E5%A4%A7%E7%89%87&comment=p.sogou.com%2Fsu%2F0HtkJu'
        headers = {
            'authority': 'discovermgs.avature.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://discovermgs.avature.net',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        }

        response = requests.request("POST", url, headers=headers, data=payload, cookies=cookies, proxies=proxies)
        if response.text.find('Mail sent successfully') == -1:
            raise ValueError('????????????')

        # text = response.text
        # print(response.status_code)
        # # ???????????? Mail sent successfully
        # # ???????????? An error has occurred
        # # ??????????????? Send to a friend
        # if text.find('Mail sent successfully') != -1:
        #     """"""
        #     logger.success('Mail sent successfully')
        #     return True
        # elif text.find('An error has occurred') != -1:
        #     logger.error('An error has occurred')
        #     return False
        # elif text.find('Send to a friend') != -1:
        #     logger.error('Send to a friend')
        #     return False
        # else:
        #     print(response.text)


def read_line(filepath: str) -> str:
    """"""

    with open(filepath, 'r', encoding='utf8') as fp:
        data = fp.read().splitlines(True)
        email = data[0].splitlines()[0]

    with open(filepath, 'w', encoding='utf8') as fp:
        fp.writelines(data[1:])

    return email


def main():
    """"""

    filepath = glob('*email*')[0]

    while True:
        email = read_line(filepath)
        print(email)


if __name__ == '__main__':
    """"""
    main()
