import os
from utils.yamlutiles import *
import yaml

# 获取项目基本目录
# 获取当前项目绝对路径
current =os.path.abspath(__file__)
# print(current)
BASE_DIR=os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)
# 定义confif目录
_config_path=BASE_DIR + os.sep + 'config'
#定义conf.yml路径
_config_file = _config_path + os.sep + 'config.yml'

def get_config_file():
    return _config_file

def get_config_path():
    return _config_path

# 读取配置文件

class configyaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = yamlreader(get_config_file()).data()
        print(self.config)
#     定义方法获取需要信息
    def get_conf_url(self):
        return self.config[0]['BASE']

if __name__=='__main__':
    conf_read = configyaml()
    print(conf_read.get_conf_url())