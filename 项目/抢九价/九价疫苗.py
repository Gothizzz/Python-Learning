# Editor: GOTHIZzz
# Dev Date: 2022/1/3
import json

import requests

# 伪装用户访问信息(通过抓包工具获得)
headers = {
    'Host': 'cloud.cn2030.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'zftsl': '69713ee662168090ef34ee1f07cf5b69',
    'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/92/page-frame.html'
}
# 访问小程序首页并且获取到所有医院信息
def get_data_all():
    url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerList&city=%5B%22%22%2C%22%22%2C%22%22%5D&lat=34.22259&lng=108.94878&id=0&cityCode=0&product=0'
    response = requests.get(url, headers=headers).json()
    print(json.dumps(response, indent=4, ensure_ascii=False))

# 获取疫苗信息
def get_data_one():
    url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=6619&lat=34.22259&lng=108.94878'
    response = requests.get(url, headers=headers).json()
    print(json.dumps(response, indent=4, ensure_ascii=False))

get_data_one()