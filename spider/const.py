#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  author  : 颜洪毅
  e-mail  : yhyzgn@gmail.com
  time    : 2018-06-02 20:55
  version : 1.0.0
  desc    : 
"""

URL = "https://www.meitulu.com"
# <a href="https://www.meitulu.com/t/nvshen/">女神</a>
PT_CATE = r'<a href="(' + URL + '/t/\w+/)">(.+)</a>'
# <p><span>52 </span>数量： 117 张(1280X850)</p>
# PT_COUNT = r'</span>数量： (\d+) 张'
PT_COUNT = r'<p><span>\d+\s*</span>数量： (\d+) 张\((\d+)X(\d+)\)</p>'
# <p class="p_title"><a href="https://www.meitulu.com/item/4613.html" target="_blank">[WPB-net] No.179 佐野雏子 《relax over the weekend》写真集</a></p>
PT_ITEM = r'<p class="p_title"><a href="(' + URL + '/item/\d+\.html)" target="_blank">(.+)</a></p>'
# <img src="https://mtl.ttsqgs.com/images/img/14258/1.jpg" alt="[XIUREN秀人] No.962 女神@小热巴甲米旅拍写真第1张" class="content_img" title="美图录提示：点击图片，查看原尺寸高清大图">
PT_IMG = r'<img src="(https://mtl.ttsqgs.com/images/img/\d+/\d+\.jpg)".*?class="content_img".*?>'
