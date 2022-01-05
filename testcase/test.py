#登录
import requests
from utils.request_utils import *
#定义登录方法
def login():
#定义测试数据
    url='http://211.103.136.242:8064/authorizations/'
    data={"username":"python","password":"12345678"}
#发送post请求
    # r=requests.post(url,data=data)
    # r=requestpost(url,json=data)
    request=Requests()
    r=request.post(url,json=data)
    print(r)
#输出结果
    # print(r.json())




def user():
    url = 'http://211.103.136.242:8064/user/'
    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE2NDEzNzIyMDcsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.QJcb2lO6egQRNdLUvmTvnhixhLxakUeMBbfSaWzPk-s'
    headers={'Authorization': 'JWT ' + token}
    # r = requests.get(url,headers=header)
    # r=requestinfo(url,headers)
    request=Requests()
    r=request.get(url,headers=headers)
    print(r)


    # print(r.json())

def goods():
    url='http://211.103.136.242:8064/categories/115/skus'
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE2NDEzNzIyMDcsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.QJcb2lO6egQRNdLUvmTvnhixhLxakUeMBbfSaWzPk-s'
    headers = {'Authorization': 'JWT ' + token}
    data={"page":"1","page_size":"10","ordering":"creat_time"}
    # r = requests.post(url,json=data,headers=headers)
    # r=requestpost(url,json=data,headers=headers)
    request = Requests()
    r = request.post(url, json=data)
    print(r)


if __name__=="__main__":
    login()
    # user()
    # goods()

