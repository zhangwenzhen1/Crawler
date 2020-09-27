import json

# json.dumps 实现python类型转化为json字符串
# indent实现换行和空格
# ensure_ascii=False实现让中文写入的时候保持为中文
# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-12-9 上午8:58 GMT+8
mydict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
        ],
    }
}

ret = json.dumps(mydict, ensure_ascii=False, indent=4)
print(ret) # json_str

ret = json.loads(ret)
print(ret)

# 把python数据类型直接的写入文件对象
with open('heihie.txt', 'w', encoding='utf-8') as f:
    # f.write(json.dumps(mydict))
    json.dump(mydict, f, ensure_ascii=False, indent=4)

# 从文件对象中直接读取json_str，返回python数据类型
with open('heihie.txt', 'r') as f:
    ret = json.load(f)
print(ret)
print(type(ret))