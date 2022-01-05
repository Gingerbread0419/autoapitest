import os
import yaml
class yamlreader:
    # 初始化，文件是否存在
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf=yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data=None
    # yaml读取
    def data(self):
        if not self._data:
            with open(self.yamlf,'r',encoding='utf-8') as f:
                self._data=list(yaml.safe_load_all(f))

                # for i in self._data:
                #
                #     print(i)
                return self._data