# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  login.py
@CreateTime:  2021-06-22
@desc: 登录获取login
@APIURL:
"""
import jsonpath
import loguru
import yaml
from common import config
from utils import my_utils, ehome_requests
import get_path_info

login_yaml = None
user_message_dic = {'token': '', 'user_id': ''}


class login_user:

    def request_url(self):
        loguru.logger.info("===开始登录===")
        # login_yaml = yaml.safe_load(open('../data_yaml/login.yaml', 'r', encoding="utf-8"))
        path = get_path_info.get_path() + '/data_yaml/login.yaml'
        login_yaml = yaml.safe_load(open(path, 'r', encoding="utf-8"))
        # 获取yaml中login内容
        login_dic = login_yaml['login']
        # 解析url的api
        login_api = login_dic['api']
        # 接口传入data
        login_data = login_dic['data']
        # 接口请求头
        login_headers = login_dic['headers']
        # url地址
        token_url = config.BASE_TEST_PATH + login_api
        http_requests = ehome_requests.HttpRequests
        login_post = http_requests.post(self, token_url, headers=login_headers, data=login_data)
        loguru.logger.info(login_post.text)
        # print(login_post.text)
        return login_post

    @staticmethod
    def get_user_message():
        login_post = login_user().request_url()
        status_code = login_post.status_code
        if status_code == config.STATUS_CODE:
            login_post_json = login_post.json()
            busiCode = str(jsonpath.jsonpath(login_post_json, '$.busiCode.'))
            if busiCode == '[0]':
                # 解析json 获得token
                data_token = str(jsonpath.jsonpath(login_post_json, '$..access_token.'))
                account_token = data_token[2:-2]
                real_token = 'bearer ' + account_token
                user_message_dic['token'] = real_token
                # 解析json 获得user_id
                user_id = my_utils.my_utils().key_string_cut(
                    str(jsonpath.jsonpath(login_post_json, '$...termAgentId.')))
                user_message_dic['user_id'] = user_id
                loguru.logger.info('=====获得token==== ：' + real_token)
                # print('=====获得token==== ：' + real_token)
            else:
                print('用户信息验证失败')
        else:
            print('登录失败')
        return user_message_dic


if __name__ == '__main__':
    print('---用户登录----')
    login_user().get_user_message()
