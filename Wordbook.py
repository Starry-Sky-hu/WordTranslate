# -*- coding: utf-8 -*-
"""
@author:StarrySky
@version:1.0
@ide:IntelliJ IDEA (Python 3.7)
@project:单词记录本
@file:Wordbook.py
@time:2020-07-16 13:04:28
@function:较上一版本在记录单词的基础上增加了谷歌翻译的功能，并不使用json写入文件
"""

import os
import http.client
import hashlib
import urllib
import random
import json
import requests

print("\nWelcome To Wordbook!  :)\n")
WordName = input("Please Enter Name of Wordbook:")
path = 'C:\\Users\\80656\\Desktop\\dictionary\\' + WordName

def PrintWords():
    with open(path, 'r') as f:
        words = f.readlines()
    for word in words:
        print(word, end='')

def AddWords():
    word = input('Enter New Word:')
    #Chinese = input('Enter Chinese of the Word:')
    TranslateResult = BaiduTranslate(word)
    print(TranslateResult)
    Chinese = TranslateResult['trans_result'][0]["dst"]
    print(Chinese)
    with open(path, 'a') as f:
        f.write(word + ':' + Chinese + '\n')

def BaiduTranslate(word):
    q = word
    fromLang = "en"
    toLang= "zh"

    appid = "20200808000537573"
    secreKey = "3bYopcdRZDFpK1h7MYE6"

    httpClient = None
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secreKey
    sign = hashlib.md5(sign.encode()).hexdigest()

    url = "/api/trans/vip/translate"
    myUrl = url + "?q=" + urllib.parse.quote(q) + "&from=" + fromLang + "&to=" + toLang + "&appid=" + appid + "&salt=" + str(salt) + "&sign=" + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET',myUrl)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

    except Exception as e:
        print(e)

    finally:
        if httpClient:
            httpClient.close()

    return result


def main():
    while True:
        mode = input("Enter Mode:\t0.Print All Words\t1.Add Word\t2.Clean the Screen\t3.Exit:\n")
        if mode == '0':
            PrintWords()
        elif mode == '1':
            AddWords()
        elif mode == '2':
            os.system('cls')
        elif mode == '3':
            break
        else:
            print('Enter False!  :(')

if __name__ == '__main__':
    main()
