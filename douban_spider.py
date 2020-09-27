# coding=utf-8
from parse import parse_url
import json
import jsonpath

class DoubanSpider(object):
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=windows&for_mobile=1&start={}&count=18&loc_id=108288&_=1600223899092"

    def get_content_list(self, html_str):
        "提取数据"
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"] # 从根节点开始，获取所有key为name的值
        list = jsonpath.jsonpath(content_list,'$..title')

        return list, total

    def save_content_list(self, content_list):
        with open("douban.txt", 'a', encoding='utf-8') as f:
            f.write(json.dumps(content_list, ensure_ascii=False))
            f.write("\n")
        print("保存成功")
    def run(self):
        num = 0
        total = 50
        while num < total + 18:
            # 1、建立开始的URL
            url = self.url.format(num)
            # print(url)
            # 2、发送请求，获取相应
            html_str = parse_url(url)
            print(html_str)
            # 3、提取数据
            content_list,total = self.get_content_list(html_str)
            # 4、保存数据
            self.save_content_list(content_list)
            # 5、构造下一页的url地址，循环2-5步
            num += 18
if __name__=='__main__':
    douban = DoubanSpider()
    douban.run()