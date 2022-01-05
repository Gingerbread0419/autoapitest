import requests
"""

def requestinfo(url,headers):
    # 发送请求
    r=requests.get(url,headers=headers)
    #获取结果
    code=r.status_code
    try:
        body=r.json()
    except Exception as e:
        body=r.text
    # 内容保存至字典
    res=dict()
    res["code"]=code
    res["body"]=body
    # 返回字典
    return res

def requestpost(url,json=None,headers=None):

    r=requests.post(url,json=json,headers=headers)

    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 内容保存至字典
    res = dict()
    res["code"] = code
    res["body"] = body
    return res
"""
class Requests:
    def requests_api(self,url,headers=None,json=None,method='get'):
        if method=='get':
            r = requests.get(url, headers=headers)
        elif method=='post':
            r = requests.post(url, json=json, headers=headers)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 内容保存至字典
        res = dict()
        res["code"] = code
        res["body"] = body
        return res
    def get(self,url,**kwargs):
        return self.requests_api(url,method='get',**kwargs)
    def post(self,url,**kwargs):
        return self.requests_api(url,method='post',**kwargs)