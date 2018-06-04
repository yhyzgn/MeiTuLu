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

# 图片保存目录（根路径）
ROOT = "D:/Files/图片/抓图/美图录"

if __name__ == "__main__":
    # 开始加载
    loader.load(ROOT)
