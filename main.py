#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  author  : 颜洪毅
  e-mail  : yhyzgn@gmail.com
  time    : 2018-06-02 20:51
  version : 1.0.0
  desc    : 程序入口
"""

from spider import loader

from spider import const
import requests

# 图片保存目录（根路径）
ROOT = "E:/图片/抓图/美图录"

if __name__ == "__main__":
    # 开始加载
    loader.load(ROOT)

    # res = requests.get("https://mtl.ttsqgs.com/images/img/14277/1.jpg", headers=const.DOWNLOADER_HEADERS)
    # print(res.status_code)
