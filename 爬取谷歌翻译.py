# -*- coding: utf-8 -*-
"""
@author:StarrySky
@version:
@ide:IntelliJ IDEA
@project:单词记录本
@file:爬取谷歌翻译.py
@time:2020-07-16 20:55:21
@function:
"""
'''
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == "__main__":
    url = 'https://translate.google.cn/#view=home&op=translate&sl=en&tl=zh-CN&text=word'
    print(getHTMLText(url))
'''

"""
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from retrying import retry

chrome_options = Options()

# 隐藏浏览器界面
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)

@retry(tries=3, delay=1)
def translate(input, target):
    base_url = 'https://translate.google.cn/#view=home&op=translate&sl=auto&tl=%s' % target

    if browser.current_url != base_url:
        browser.get(base_url)

    submit = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="source"]')))
    submit.clear()
    submit.send_keys(input)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="tlid-translation translation"]')))
    source = etree.HTML(browser.page_source)
    result = source.xpath('//span[@class="tlid-translation translation"]//text()')[0]

    return result


if __name__ == '__main__':
    for i in range(100):
        print(translate('中英翻译测试', target='en'))
        print(translate('再测试一下', target='en'))
        print(translate('hello world', target='zh-CN'))
    browser.quit()
"""

import requests
import json
from bs4 import BeautifulSoup
import execjs  # 必须，需要先用pip 安装，用来执行js脚本


class Py4Js():
    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
        """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def buildUrl(text, tk):
    BaseUrl = 'https://translate.google.cn/translate_a/single'
    BaseUrl += '?client=t&'
    BaseUrl += 's1=auto&'
    BaseUrl += 't1=zh-CN&'
    BaseUrl += 'h1=zh-CN&'
    BaseUrl += 'dt=at&'
    BaseUrl += 'dt=bd&'
    BaseUrl += 'dt=ex&'
    BaseUrl += 'dt=ld&'
    BaseUrl += 'dt=md&'
    BaseUrl += 'dt=qca&'
    BaseUrl += 'dt=rw&'
    BaseUrl += 'dt=rm&'
    BaseUrl += 'dt=ss&'
    BaseUrl += 'dt=t&'
    BaseUrl += 'ie=UTF-8&'
    BaseUrl += 'oe=UTF-8&'
    BaseUrl += 'otf=1&'
    BaseUrl += 'pc=1&'
    BaseUrl += 'ssel=0&'
    BaseUrl += 'tsel=0&'
    BaseUrl += 'kc=2&'
    BaseUrl += 'tk=' + str(tk) + '&'
    BaseUrl += 'q=' + text
    return BaseUrl


def translate(text):
    header = {
        'authority': 'translate.google.cn',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36','x-client-data':'CIa2yQEIpbbJAQjBtskBCPqcygEIqZ3KAQioo8oBGJGjygE='
    }
    url = buildUrl(text, js.getTk(text))
    res = ''
    try:
        r = requests.get(url, headers=header)
        result = json.loads(r.text)
        if result[7] != None:
            # 如果我们文本输错，提示你是不是要找xxx的话，那么重新把xxx正确的翻译之后返回
            try:
                correctText = result[7][0].replace('<b><i>', ' ').replace('</i></b>', '')
                print(correctText)
                correctUrl = buildUrl(correctText, js.getTk(correctText))
                correctR = requests.get(correctUrl)
                newResult = json.loads(correctR.text)
                res = newResult[0][0][0]
            except Exception as e:
                print(e)
                res = result[0][0][0]
        else:
            res = result[0][0][0]
    except Exception as e:
        res = ''
        print(url)
        print("翻译" + text + "失败")
        print("错误信息:")
        print(e)
    finally:
        return res


if __name__ == '__main__':
    js = Py4Js()
    res = translate('圣诞节')
    print(res)