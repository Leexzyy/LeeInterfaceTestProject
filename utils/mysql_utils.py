# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  mysql_utils.py
@CreateTime:  2021-08-19
@desc: TODO 创建pymysql类
"""
import pymysql

class HandleDB:

    def __init__(self):
        # 读取配置文件的数据库信息
        self.con = pymysql.connect(host=conf.get_str("mysql", "host"),
                                   user=conf.get_str("mysql", "user"),
                                   password=conf.get_str("mysql", "password"),
                                   port=conf.get_int("mysql", "port"),
                                   charset="utf8"
                                   )
        self.cur = self.con.cursor()

    def get_one(self, sql):
        """获取查询到的第一条数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self, sql):
        """获取sql语句查询到的所有数据"""
        pass

    def count(self, sql):
        """统计sql语句查询到的数据"""
        pass

    def close(self):
        self.cur.close()  # 关闭游标对象
        self.con.close()  # 断开连接
