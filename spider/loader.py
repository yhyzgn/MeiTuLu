#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  author  : 颜洪毅
  e-mail  : yhyzgn@gmail.com
  time    : 2018-06-02 20:54
  version : 1.0.0
  desc    : 
"""

from . import const
import requests
import re


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
    return re.findall(const.PT_ITEM, html)


def get_item_count_attrs(html):
    """
    获取所有item的数量和属性
    :param html: html代码
    :return: item的数量和属性
    """
    return re.findall(const.PT_COUNT, html)

def get_imgs(html):
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
        return pagesize, 0
    return pagesize, int(total[0])


def get_item_list_page_count_of_cate(url):
    """
    获取每个分类下item中的总页数
    :return: 总页数
    """
    result = get_item_list_size_and_total_of_cate(url)
    pagesize = result[0]
    total = result[1]
    if total == 0:
        return 1
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


def load():
    """
    加载所有数据
    :return: null
    """

    # 先获取所有分类
    cateList = get_cate_list(req())

    # 遍历每个分类，再去获取分类下的item列表，最后将每个分类下的页数添加到对应分类中
    for i in range(0, len(cateList)):
        pageCount = get_item_list_page_count_of_cate(cateList[i][0])
        temp = list(cateList[i])
        temp.append(pageCount)
        cateList[i] = tuple(temp)

        # print(cateList[i][1] + " : " + str(pageCount) + " 页")
        # print(cateList[i])

        # 将分类下的所有分页子url和每个子url页面中对应的item列表都放到该分类的元组中
        cateList[i] = get_item_list_of_cate(cateList[i])
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(cateList[i])
        # 目前为止，已经将每个分类下的item列表html页面url全部拿到
        # ('https://www.meitulu.com/t/nvshen/', '女神', 30, ['cate/2.html','cate/3.html'], [('https://www.meitulu.com/item/13585.html', '[MICAT瑞丝馆] Vol.037 清纯甜美妹子@米粒sweet'),()])

    return ""
