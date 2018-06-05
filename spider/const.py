#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  author  : 颜洪毅
  e-mail  : yhyzgn@gmail.com
  time    : 2018-06-02 20:55
  version : 1.0.0
  desc    : 一些常量
"""

URL = "https://www.meitulu.com"
# https://mtl.ttsqgs.com/images/img/1850/5.jpg
IMG_URL = "https://mtl.ttsqgs.com/images/img/"
# <a href="https://www.meitulu.com/t/nvshen/">女神</a>
PT_CATE = r'<a href="(' + URL + '/t/\w+/)">(.+)</a>'
# <p><span>9</span>图片： 40 张(1600X2400)</p>...<p class="p_title"><a href="https://www.meitulu.com/item/4613.html" target="_blank">[WPB-net] No.179 佐野雏子 《relax over the weekend》写真集</a></p>
PT_ITEM = r'<p><span>\d+\s*</span>图片： (\d+) 张\((\d+)X(\d+)\)</p>.*?<p class="p_title"><a href="(' + URL + '/item/\d+\.html)" target="_blank">(.+?)</a></p>'
# <img src="https://mtl.ttsqgs.com/images/img/14258/1.jpg" alt="[XIUREN秀人] No.962 女神@小热巴甲米旅拍写真第1张" class="content_img" title="美图录提示：点击图片，查看原尺寸高清大图">
PT_IMG = r'<img src="(https://mtl.ttsqgs.com/images/img/\d+/\d+\.jpg)".*?class="content_img".*?>'
# https://www.meitulu.com/item/14277.html
PT_ITEM_ID = r'https://www\.meitulu\.com/item/(\d+)\.html'
# 下载图片时的请求头
DOWNLOADER_HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                      "Accept-Encoding": "gzip, deflate, br",
                      "Accept-Language": "zh-CN,zh;q=0.9",
                      "Cache-Control": "no-store",
                      "Connection": "keep-alive",
                      "Host": "mtl.ttsqgs.com",
                      # "If-Modified-Since": "Wed, 05 Jul 2017 10:48:00 GMT",
                      # "If-None-Match": "f847bc2b7cf5d21:0",
                      "Upgrade-Insecure-Requests": "1",
                      "Referer": "https://www.meitulu.com/item/14258.html",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
