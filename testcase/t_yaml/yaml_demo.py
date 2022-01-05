import yaml
#读取单个文档
# with open('./data.yml','r') as f:
#     r=yaml.safe_load(f)
#     print(r)
# 读取多个文档
# with open('./data.yml','r',encoding='utf-8') as f:
#     r=yaml.safe_load_all(f)
#
#     for a in r:
#         print(a)
from utils.yamlutiles import *

res=yamlreader('./data.yml').data()
print(res)


