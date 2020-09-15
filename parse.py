# utf-8
import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.102 Safari/537.36",
    # "Host": "www.baidu.com",
    "Cookie": "BIDUPSID=286613A70588224F8DB57ADE2EF3C9E4; PSTM=1574049951; BAIDUID=286613A70588224FC0244BA4EF77A94D:FG=1; "
              "BD_UPN=12314753; BDUSS=dhNVJtNn5LLUxpUko5MkpzOTNsV21obHFoZElBZE8teTV0UDV2b0lwUlhMZnRkRVFBQUFBJCQAAAAA"
              "AAAAAAEAAADUGTEjd2VuemhlbjkzOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFeg"
              "011XoNNdLV; BDUSS_BFESS=dhNVJtNn5LLUxpUko5MkpzOTNsV21obHFoZElBZE8teTV0UDV2b0lwUlhMZnRkRVFBQUFBJCQAAAAAAAA"
              "AAAEAAADUGTEjd2VuemhlbjkzOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFeg011X"
              "oNNdLV; H_WISE_SIDS=154034_148078_153759_150830_153190_149355_150686_150075_156287_150086_148867_154763_"
              "156087_154605_151897_153628_153444_154771_151532_151018_154950_146575_127969_154413_154175_152982_155905"
              "_155802_146732_155789_131423_154037_154786_155539_154189_154791_144966_155354_155531_154619_154118_154802"
              "_154903_155238_155932_154146_147552_156101_153448_152310_155390_154349_155865_110085; BDORZ=FFFB88E99905"
              "5A3F8A630C64834BD6D0; plus_cv=1::m:49a3f4a6; yjs_js_security_passport=7c04e2b4f2bd985d8b852896e116920a720"
              "5f87d_1600072536_js; H_PS_PSSID=32606_7523; H_PS_645EC=4160ziOuxMZS8by7rZnTpROCkgiU%2FR4AzL7Q%2FlKcq98Dww"
              "Rqcz6K2KqcO6gifDy2qlq6JIxfbYQ; delPer=0; BD_CK_SAM=1; PSINO=1; BDRCVFR[B3iNXbc_kLT]=OjjlczwSj8nXy4Grjf8m"
              "vqV; BD_HOME=1",
    # "Referer": "https://www.baidu.com/?tn=78000241_12_hao_pg"
    }

def retry_if_result_none(result):
    return result is None

'''专门请求URL的方法'''
@retry(stop_max_attempt_number=3,retry_on_result = retry_if_result_none) #让装饰函数反复执行三次，三次全部报错才会报错，中间有一次正常，则程序继续执行
def _parse_urlq(url):
    print("*" * 100)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_urlq(url)
    except:
         html_str = None
    return html_str

if __name__ == '__main__':
    url = "https://www.baidu.com"
    print(parse_url(url)[:100])
