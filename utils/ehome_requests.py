# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  ehome_requests.py
@CreateTime:  2021-07-21
@desc: 封装requests方法
@APIURL:
"""
import loguru
from common import config
import requests


class HttpRequests:
    __instance = None

    def __init__(self):
        self.session = requests.session()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(HttpRequests, cls).__new__(cls)
        return cls.__instance

    def get(self, url, headers=None, params=None):
        """
        GET请求
        基于requests库进行关键字驱动封装
        :param: url 传入的url
        :param: headers 传入的  请求头  可为NONE
        :param: params 传入的   请求体  可为NONE
        """
        return requests.get(url=url, headers=headers, params=params)

    def post(self, url, headers=None, data=None, json=None):
        """
        GET请求
        基于requests库进行关键字驱动封装
        :param: url     传入的url
        :param: headers 传入headers       可为空
        :param: data    传入的 data       可为空
        :param: json    传入的 json       可为空
        """
        if data is None:
            return requests.post(url=url, headers=headers, json=json)
        elif json is None:
            return requests.post(url=url, headers=headers, data=data)
        elif data is None and json is None:
            return requests.post(url=url, headers=headers)

    def all_requests(self, **kwargs):
        """
        封装requests内容  可以动态解析传入方法且可以直接解析yaml文件 但是需要遵循规定的YAML格式
        :param: kwargs  传入规定格式的yaml文件 详情请参考接口测试约定文档
        """
        method = kwargs.get('method')
        api = kwargs.get('api')
        headers = kwargs.get('headers')
        data = kwargs.get('data')
        json = kwargs.get('json')
        params = kwargs.get('params')
        if method is None:
            loguru.logger.error('此接口传入method有误且为必填项 请检查YAML文件是否符合规范')
        if api is None:
            loguru.logger.error('此接口传入api有误且为必填项 请检查YAML文件是否符合规范')
        if headers is None:
            loguru.logger.error('此接口传入headers有误且为必填项 请检查YAML文件是否符合规范')
        try:
            request = self.session.request(method=method, url=config.BASE_TEST_PATH + api, headers=headers, data=data,
                                           json=json, params=params)
        except Exception as e:
            loguru.logger.error("requests 请求错误 : %s" % e)

        return request


if __name__ == '__main__':
    get = HttpRequests().get_session()
