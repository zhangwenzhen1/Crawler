# coding=utf-8
from lxml import etree
import requests
url = "https://movie.douban.com/chart"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
response = requests.get(url,headers=headers)
html_str = response.content.decode()
# print(html_str)
#使用etree处理数据
html = etree.HTML(html_str)
print(html)
# 1、获取所有的电影url地址
url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")
# print(url_list)
# 2、获取所有图片的url地址
img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
print(img_list)
#3、把每部电影组成一个字典，字典中是电影的更新数据，比如标题，url,图片地址，评论数，评分
##3.1 分组
retl = html.xpath("//div[@class='indent']/div/table")
print(retl)

for table in retl :
    item = {}
    ##防止抓取内容为空报错，用if else语句做是否为空判断
    item["title"] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()  \
        if len(table.xpath(".//div[@class='pl2']/a/text()")[0]) >0 else None
    item["href"] = table.xpath(".//div[@class='pl2']/a/@href")[0] if len(table.xpath(".//div[@class='pl2']/a/@href")[0])\
                                                                     >0 else None
    item["img"] = table.xpath(".//a[@class='nbg']/img//@src")[0]  if len(table.xpath(".//a[@class='nbg']/img//@src")[0])\
                                                                     > 0 else None
    item["comment_num"] = table.xpath("//span[@class='pl']/text()")[0] if len(table.xpath("//span[@class='pl']/text()")
                                                                              [0]) >0 else None
    item["rating_num"] = table.xpath("//span[@class='rating_nums']/text()")[0]\
        if len(table.xpath("//span[@class='rating_nums']/text()")[0])>0 else None
    print(item)
