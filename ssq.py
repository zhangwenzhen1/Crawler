# 分析网页后可以得知get历史所有数据的参数
url = 'https://datachart.500.com/ssq/history/newinc/history.php?start=03001'

# 加载相关的库
import requests
import numpy as np
import pandas as pd
from lxml import etree
# 获取历史所有双色球数据
response = requests.get(url)
# response.encoding = 'utf-8'
html_str = response.content.decode("utf-8")
print(type(html_str))
with open("123.xml",'w',encoding='utf-8') as f:
    f.write(html_str)
# print(html_str)
re_text = response.text
# e= etree.HTML(re_text)

# 网页数据解析
re = re_text.split('<tbody id="tdata">')[1].split('</tbody>')[0]
result = re.split('<tr class="t_tr1">')[1:]

all_numbers = []
for i in result:
    each_numbers = []
    i = i.replace('<!--<td>2</td>-->', '')
    each = i.split('</td>')[:-1]
    for j in each:
        each_numbers.append(j.split('>')[1].replace('&nbsp;', ''))

    all_numbers.append(each_numbers)

# 定义列名称
col = ['期号', '红球1', '红球2', '红球3', '红球4', '红球5', '红球6', '蓝球', '快乐星期天', '奖池奖金(元)',
       '一等奖注数', '一等奖奖金(元)', '二等奖注数', '二等奖奖金(元)', '总投注额(元)', '开奖日期']

# 解析完网页数据，生成双色球数据框
df_all = pd.DataFrame(all_numbers, columns=col)
df_all.replace(',', '')
df_all.to_csv('./shangseqiu.csv',encoding='gbk',index=False)
# 输出第1到4行
print(df_all.iloc[1:5])
df = df_all.head()
print(df_all.head())
print(df_all.iloc[:, 0].size)

df = df[['红球1', '红球2', '红球3', '红球4', '红球5', '红球6']]
# df123 = df.groupby(['红球1', '红球2', '红球3', '红球4', '红球5', '红球6'])['期号'].agg([len,np.sum])
# df123.to_csv('./shangseqiu123.csv',encoding='gbk')
print(df.iloc[:, 0].size)
print(df.head())

x = df.values
m = []

for _ in x:
    y = _
    # print(y)
    for i in y:
        i = int(i)
        m.append(i)
print(set(m))

mm =[]
for j in range(1,34):
    if j not in set(m):
        mm.append(j)
print(mm)

from scipy.special import comb, perm
print("双色球组合种类数",comb(33,6) * 16)
