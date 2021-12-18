# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  my_utils.py
@CreateTime:  2021-08-03
@desc:
@APIURL:
"""

import jsonpath
import random


class my_utils():
    # 裁剪string类型的内容
    def key_string_cut(self, key):
        return key[2:-2]

    # 封装jsonpath
    def get_json(self, json, key):
        return jsonpath.jsonpath(json, key)

    def json_string(self, json, key):
        return my_utils.get_json(self, json, key)[0]

    def json_int(self, json, key):
        return my_utils.get_json(self, json, key)[0]

    # 随机生成15位数字的订单号
    @staticmethod
    def random_order_num():
        return ''.join((str(random.choice(range(10))) for _ in range(15)))


if __name__ == '__main__':
    print(my_utils.random_order_num())
