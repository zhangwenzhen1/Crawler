
from urllib.parse import quote
from urllib import request
import json
import xlwt

amap_web_key = 'e96f9a501924b3475e1e9335477e8083' # 高德地图key
poi_search_url = "https://restapi.amap.com/v3/place/text"
poi_boundary_url ="https://restapi.amap.com/v3/place/detail"


# 根据id获取边界数据
def getBounById(id):
    req_url = poi_boundary_url + "?key=" + amap_web_key + "?id=" + id
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
        dataList = []
        datajson = json.loads(data)  # 将字符串转换为json
        print(datajson)
        datajson = datajson['data']
        datajson = datajson['spec']
        if len(datajson) == 1:
            return dataList
        if datajson.get('mining_shape') != None:
            datajson = datajson['mining_shape']
            shape = datajson['shape']
            dataArr = shape.split(';')

            for i in dataArr:
                innerList = []
                f1 = float(i.split(',')[0])
                innerList.append(float(i.split(',')[0]))
                innerList.append(float(i.split(',')[1]))
                dataList.append(innerList)
        return dataList

#单页获取pois
def getpoi_page(cityname, keywords, page):
    req_url = poi_search_url + "?key=" + amap_web_key + '&extensions=all&keywords=' + quote(keywords) + '&city=' + quote(cityname) + '&citylimit=true' + '&offset=25' + '&page=' + str(page) + '&output=json'
    data = ''
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    return data

#根据城市名称和分类关键字获取poi数据
def getpois(cityname, keywords):
    i = 1
    poilist = []
    while True : #使用while循环不断分页获取数据
       result = getpoi_page(cityname, keywords, i)
       result = json.loads(result)  # 将字符串转换为json
       if result['count'] == '0':
           break
       poilist.extend(result['pois'])
       i = i + 1
    return poilist


#获取城市分类数据
cityname = "北京"
classfiled = "大学"
pois = getpois(cityname, classfiled)
####
dataList = getBounById('B02F4027LY')