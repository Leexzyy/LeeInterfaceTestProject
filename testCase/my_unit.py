# # -*- coding:utf-8 -*-
# """
# @Author: Leexzyy
# @File:  my_unit.py
# @CreateTime:  2021-09-24
# @desc:  封装Unittest
# @API_URL:  http://test-client.ehomepoct.com/doc.html#/payment-center/%E6%94%AF%E4%BB%98%E7%AE%A1%E7%90%86/prePayUsingPOST"""
#
import unittest
import warnings
import loguru
from ddt import ddt, file_data
from utils import ehome_requests

my_log = loguru.logger


@ddt
class TestUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        my_log.info("在这个类开始时初始化")

    @classmethod
    def tearDownClass(cls):
        my_log.info("在这个类结束时清除")

    def setUp(self):
        # 忽略危险提示信息
        warnings.simplefilter('ignore', ResourceWarning)
        my_log.info("在这个类结束时清除")

    def tearDown(self):
        my_log.info("在case结束时清除")
