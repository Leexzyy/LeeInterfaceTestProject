# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  log_utils.py
@CreateTime:  2021-07-27
@desc: 基于loguru进行日志模块封装
"""

from loguru import logger
import time
import get_path_info


def logger_config():
    t = time.strftime("%Y-%m-%d")
    time_name = time.strftime('%H：%M：%S')

    log_path = get_path_info.get_path() + '/log/' + t
    logger.add(f"{log_path}/{time_name}.log",
               rotation="500MB",  # 最大保存大小
               encoding="utf-8",  # 支持中文格式
               enqueue=True,  # 支持异步存储
               retention="10 days",  # 配置日志的最长保留时间
               format="[{time:YYYY-MM-DD HH:mm:ss} {level:<8} | {file}:{line}]  {message}"  # 日誌样式
               )


class Loggings(object):
    __instance = None

    # 单列模式
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    logger_config()

    def info(self, msg):
        class_name = self.__class__.__name__
        self.__str__()
        return logger.info(class_name + '.py  |  ' + msg)

    def debug(self, msg):
        class_name = self.__class__.__name__
        return logger.debug(class_name + '.py  |  ' + msg)

    def warning(self, msg):
        class_name = self.__class__.__name__
        return logger.warning(class_name + '.py  |  ' + msg)

    def error(self, msg, sys):
        class_name = self.__class__.__name__
        return logger.error(class_name + '.py  |  ' + msg)

    def success(self, msg, sys):
        class_name = self.__class__.__name__
        return logger.success(class_name + '.py  |  ' + msg)


if __name__ == '__main__':
    pass
