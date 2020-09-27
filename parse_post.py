import requests
from retrying import retry

# 实例化session
session = requests.session()

# 使用session发送post请求，获取对方保存在本地的cookie
post_url = "http://www.renren.com/PLogin.do"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
post_data ={"email":"*******@qq.com","password":"********"}
session.post(post_url,headers=headers,data=post_data)
#在使用session请求登录后的界面
url = "http://www.renren.com/301215613/profile"
response = session.get(url,headers=headers)
with open ("renren.html","w",encoding='utf-8') as f:
    f.write(response.content.decode())