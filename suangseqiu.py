import requests
from lxml import etree
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
url = 'https://datachart.500.com/ssq/?expect=50'

response = requests.get(url, headers=headers)
html_str = response.content.decode("gbk")
# print(html_str)
e= etree.HTML(html_str)

nos = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
print(len(nos))
print(nos)
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')
print(trs)
# record = 0
#xh-highlight
# print('要执行的任务条数:',record)
for i in range(len(nos)):
    rb='-'.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    bb = trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    print('插入数据:', nos[i], ':', rb, bb)
