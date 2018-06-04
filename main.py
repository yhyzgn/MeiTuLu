#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  author  : 颜洪毅
  e-mail  : yhyzgn@gmail.com
  time    : 2018-06-02 20:51
  version : 1.0.0
  desc    : 
"""

from spider import loader
import requests

ROOT = "E:/图片/抓图/美图录"

if __name__ == "__main__":
    # html = loader.req("https://www.meitulu.com/t/nvshen/30.html")
    # print(html)
    # cateList = loader.get_cate_list(html)
    # print(cateList)
    #
    # itemList = loader.get_item_list(html)
    # print(itemList)

    # res = loader.get_item_list_page_count_of_cate("https://www.meitulu.com/t/nvshen/")
    # print(res)

    loader.load()

    # html = loader.req("https://www.meitulu.com/item/14258_3.html")
    # imgList = loader.get_imgs(html)
    # print(imgList)

    # headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #            "Accept-Encoding": "gzip, deflate, br",
    #            "Accept-Language": "zh-CN,zh;q=0.9",
    #            "Cache-Control": "max-age=0",
    #            "Connection": "keep-alive",
    #            "Host": "mtl.ttsqgs.com",
    #            "If-Modified-Since": "Wed, 05 Jul 2017 10:48:00 GMT",
    #            "If-None-Match": "f847bc2b7cf5d21:0",
    #            "Upgrade-Insecure-Requests": "1",
    #            "Referer": "https://www.meitulu.com/item/14258.html",
    #            "User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
    #
    # res = requests.get("https://mtl.ttsqgs.com/images/img/14258/41.jpg", headers=headers)
    # print(res)
    # with open("test.jpg", "wb") as f:
    #     f.write(res.content)

    # print(loader.get_item_id("https://www.meitulu.com/item/14277.html"))

    print(loader.md5("123456"))
