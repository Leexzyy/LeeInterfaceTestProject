# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  test_demo.py
@CreateTime:  2021-07-26
@desc:
@APIURL:
"""

from my_unit import TestUnit
import jsonpath
from ddt import ddt, file_data
from utils import ehome_requests, my_utils
import loguru
from common import config

my_log = loguru.logger
utils = my_utils.my_utils

@ddt
class test_yaml_demo(TestUnit):

    @file_data('../data_yaml/test.yaml')
    def test_01(self, **kwargs):
        # 固定写法 增加测试报告的描述内容
        desc = kwargs['desc']
        self._testMethodDoc = desc
        # requests请求实例化
        all_requests = ehome_requests.HttpRequests().all_requests(**kwargs)
        # 打印请求出来的结果
        print(all_requests.text)
        # 打印日志 如果只是记录内容的话就使用info等级
        my_log.info(all_requests.text)
        # 获取接口返回状态码
        code = all_requests.status_code
        # 做判断是否是正确的状态码
        if code == config.STATUS_CODE:
            # 实例化接口请求的内容格式化为json
            requests_json = all_requests.json()
            # 解析出bushicode码 断言是否为约定值
            busi_code = utils.json_int(self, requests_json, '$.busiCode')
            # 获取yaml文件中断言码
            bushicode = kwargs['assert']['busicode']
            # 断言是否为期望值
            self.assertEqual(busi_code, bushicode, 'bushicode错误')
            if busi_code == bushicode:
                #解析出json内容
                msg = utils.json_string(self, requests_json, '$.msg')
                # 获取yaml内容
                my_msg = kwargs['assert']['msg']
                self.assertEqual(msg,my_msg,'msg与预期不符')
            #     后续需要断言data
            else:
                my_log.warning('接口请求bushicode有误')
        else:
            my_log.warning('接口请求失败')

    def test_02(self):
        my_log.info('test_02')


if __name__ == '__main__':
    print("开始接口测试")
    unittest.main()
