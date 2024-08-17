
import unittest
from unittest.mock import patch
import requests

class CalculateStandardWeight(unittest.TestCase):
    def setUp(self):
        # 设置API Key和基础URL
        self.api_key = '7760261f9d9f2f6dba856ab8cf717217'
        self.base_url = 'http://apis.juhe.cn/fapig/calculator/weight'

    def test_calculate_standard_weight(self):
        # 接口请求入参配置
        requestParams = {
            'key': self.api_key,
            'sex': '2',
            'role': '1',
            'height': '163.6666',
            'weight': '42',
        }

        response = requests.get(self.base_url, params=requestParams)

        # 解析响应结果
        if response.status_code == 200:
            responseResult = response.json()
            # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
            print(responseResult)
            self.assertEqual(responseResult['result']['idealWeight'], 55.8)
            self.assertEqual(responseResult['result']['levelMsg'], '偏瘦')
        else:
            # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
            print('请求异常')

if __name__ == '__main__':
    unittest.main()

