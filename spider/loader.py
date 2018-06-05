#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  author  : 颜洪毅
  e-mail  : yhyzgn@gmail.com
  time    : 2018-06-02 20:54
  version : 1.0.0
  desc    : 加载器
"""

from . import const
import requests
import re
import hashlib
import os


def req(url=const.URL):
    """
    通过URL加载数据
    :param url: 地址
    :return: html代码
    """
    res = requests.get(url)
    res.encoding = "utf-8"
    return res.text


def get_url():
    """
    获取根URL
    :return: 根URL
    """
    return const.URL


def get_cate_list(html):
    """
    获取所有的分类列表
    :param html: html代码
    :return: 分类列表
    """
    return re.findall(const.PT_CATE, html)


def get_item_list(html):
    """
    获取所有的item列表
    :param html: html代码
    :return: item列表
    """
    return re.findall(const.PT_ITEM, html.replace("\n", ""))


def get_imgs(html):
    """
    获取图片地址
    :param html: html代码
    :return: 图片地址列表
    """
    return re.findall(const.PT_IMG, html)


def get_item_list_size_and_total_of_cate(url):
    """
    获取每个分类下item每页显示的数量和数据总条数
    :param url: item地址
    :return: 每页大小和总条数
    """
    html = req(url)
    res = re.findall(r'<ul class="img">.*?</ul>', html.replace("\n", ""))
    pagesize = len(re.findall(r'<li>', res[0]))
    total = re.findall(r'<a class="a1">(\d+)条</a>', html)
    if len(total) == 0:
        return pagesize, pagesize
    return pagesize, int(total[0])


def get_item_list_page_count_of_cate(item_count):
    """
    获取每个分类下item中的总页数
    :param item_count: 条目数量
    :return: 总页数
    """
    pagesize = item_count[0]
    total = item_count[1]
    return int((total + pagesize - 1) / pagesize)


def get_item_list_of_cate(cate):
    """
    获取每个分类下的item列表
    :param cate: 分类元组
    :return: 所有item列表
    """
    urls = []
    itemList = []
    for i in range(0, cate[2]):
        url = get_item_list_page_urls(i, cate)

        urls.append(url)

        # 加载每个cate下的每一页item列表
        itemList += get_item_list(req(url))
    cate = list(cate)
    cate.append(urls)
    cate.append(itemList)
    return tuple(cate)


def get_item_list_page_urls(index, cate):
    """
    获取分类的每个分页子url
    :param index: 当前索引
    :param cate: 分类
    :return: 具体地址
    """
    url = cate[0]
    if index > 0:
        url += str(index + 1) + ".html"
    return url


def get_item_page_urls(cate):
    """
    获取分类下所有分页的链接
    :param cate: 一个分类
    :return: 加入所有分页后的分类
    """
    items = cate[4]
    for i in range(0, len(items)):
        itemUrl = items[i][0]
        itemName = items[i][1]
        temp = list(items[i])
        urls = []

        for j in range(0, cate[2]):
            if j > 0:
                itemUrl = items[i][0].replace(".html", "_" + str(j + 1) + ".html")
            urls.append(itemUrl)

        temp.append(urls)
        items[i] = tuple(temp)


def get_item_id(url):
    """
    获取item的id编号
    :param url: item第一页的链接
    :return: 编号
    """
    return re.findall(const.PT_ITEM_ID, url)


def get_img_list_all(cate):
    """
    获取一个分类下的所有图片地址
    :param cate: 一个分类
    :return: 将图片地址加入当前分类，并返回
    """
    data = cate[4]
    for i in range(len(data)):
        imgCount = int(data[i][0])
        itemId = get_item_id(data[i][3])
        imgList = []
        for j in range(0, imgCount):
            imgList.append(const.IMG_URL + itemId[0] + "/" + str(j + 1) + ".jpg")
        temp = list(cate[4][i])
        temp.append(imgList)
        cate[4][i] = tuple(temp)
    return cate


def md5(content):
    """
    MD5加密
    :param content: 原始内容
    :return: 加密后的内容
    """
    md5 = hashlib.md5()
    md5.update(content.encode(encoding="utf-8"))
    return md5.hexdigest()


def download_img(path, url, item):
    """
    下载图片
    :param path: 保存路径
    :param url: 下载地址
    :param item: 所属条目
    :return: None
    """
    imgName = path + "/" + md5(url) + ".jpg"

    if os.path.exists(imgName):
        # 图片已经存在
        return
    headers = const.DOWNLOADER_HEADERS
    headers["Referer"] = item[3]

    res = requests.get(url, headers=headers)
    with open(imgName, "wb") as f:
        f.write(res.content)
    res.close()

    print(item[4] + " [" + url + "] 已下载到 [" + imgName + "]")


def load(root=""):
    """
    加载所有数据
    :param root: 保存路径
    :return: None
    """

    root = root.strip("\\").strip("/")
    data = []

    print("正在获取资源，可能需要等待几分钟...")

    # 先获取所有分类
    cateList = get_cate_list(req())

    # 遍历每个分类，再去获取分类下的item列表，最后将每个分类下的页数添加到对应分类中
    for i in range(0, len(cateList)):
        itemCount = get_item_list_size_and_total_of_cate(cateList[i][0])
        pageCount = get_item_list_page_count_of_cate(itemCount)
        temp = list(cateList[i])
        temp.append(pageCount)
        cateList[i] = tuple(temp)

        # 将分类下的所有分页子url和每个子url页面中对应的item列表都放到该分类的元组中
        cateList[i] = get_item_list_of_cate(cateList[i])

        # 目前为止，已经将每个分类下的item列表html页面url全部拿到
        cateList[i] = get_img_list_all(cateList[i])

        # cateList[i][0] -> 分类第一页连接
        # cateList[i][1] -> 分类名称
        # cateList[i][2] -> 分类下条目总数
        # cateList[i][3] -> 分类下所有分页连接
        # cateList[i][4] -> 分类下所有条目信息（图片张数，图片宽，图片高，条目第一页连接，条目名称，条目中的所有图片地址）

        cate = {
            "name": cateList[i][1],
            "itemCount": itemCount[1],
            "items": cateList[i][4]
        }

        data.append(cate)

    del cateList

    print("资源获取完成，开始下载...")

    for i in range(0, len(data)):
        # 创建分类目录——女神（30）
        cateDir = root + "/" + data[i]["name"] + "（" + str(data[i]["itemCount"]) + "）"
        if not os.path.exists(cateDir):
            os.makedirs(cateDir)

        items = data[i]["items"]
        for j in range(0, len(items)):
            itemDir = cateDir + "/" + "[" + str(j + 1) + "]" + items[j][4] + "_" + items[j][0] + "张_" + items[j][1] + "x" + items[j][2]
            if not os.path.exists(itemDir):
                os.makedirs(itemDir)

            imgs = items[j][5]
            for k in range(0, len(imgs)):
                download_img(itemDir, imgs[k], items[j])

    print("所有图片下载完成！")
