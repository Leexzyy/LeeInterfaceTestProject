# -*- coding:utf-8 -*-
"""
@Author: Leexzyy
@File:  send_email_report.py
@CreateTime:  2021-06-11
@desc: 发送邮件类
"""
import yagmail
import os
import time

from common import config

get_cwd = os.getcwd()
my_file = get_cwd + "\EHomeInterfaceTest.html"
title_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class SendEmail():

    def yagmail(self, file, correct_rate):
        print('正在发送测试报告')
        try:
            yag = yagmail.SMTP(user=config.EMAIL_USER, password=config.EMAIL_PWD, host=config.EMAIL_HOST)
            yag.send(
                # to 收件人，如果一个收件人用字符串，多个收件人用列表即可
                # to=['294062541@qq.com', '247178756@qq.com', 'lijiangtao999@dingtalk.com'],
                to=config.EMAIL_RECIPIENT,
                # cc 抄送，含义和传统抄送一致，使用方法和to 参数一致
                cc=config.EMAIL_CC,
                # subject 邮件主题（也称为标题）
                subject=title_time + config.EMAIL_TITLE + f"通过率:{correct_rate}%",
                # contents 邮件正文
                contents="""
                    执行测试中……
                    测试已完成！！
                    生成报告中……
                    报告已生成……
                    报告已邮件发送！！
                    """,
                # attachments 附件，和收件人一致，如果一个附件用字符串，多个附件用列表
                attachments=[file])
            print('send email ok!!!!')

        finally:
            # 记得关掉链接，避免浪费资源
            yag.close()


if __name__ == '__main__':
    print('发送Email')
    SendEmail().yagmail(my_file)
    print('发送成功')
