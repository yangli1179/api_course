# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/14

E-mail:1179384105@qq.com

=================================


"""


import smtplib
from email.mime.text import MIMEText        # 构造邮件文本内容
from email.header import Header      # 构造邮件标题
from email.mime.application import MIMEApplication      # 发送带附件的邮件
from email.mime.multipart import MIMEMultipart      # 发送带附件的邮件
from common.config import conf
import logging
from common import logger

class SendEmail(object):

    @staticmethod
    def send_qq_file_email(title, message, file_path):
        # 创建一个smtp对象，并连接smtp服务
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)

        # 登录smtp服务器
        sender = conf.get("email", "sender")
        password = conf.get("email", "password")
        s.login(user=sender, password=password)

        # 将str类型转换成list
        recipient = eval(conf.get("email", "recipient"))

        # 构建邮件内容
        # 创建一个邮件文本类型
        content = MIMEText(message, _charset="utf8")

        # 构造附件
        part = MIMEApplication(open(file_path, "rb").read(), _subtype=False)   # rb是只读二进制文件
        part.add_header("content-disposition", "attachment", filename="report.html")

        # 封装邮件，添加邮件主题
        msg = MIMEMultipart()

        # 添加文本内容和附件
        msg.attach(content)
        msg.attach(part)

        msg["Subject"] = Header(title, "utf8")
        msg["From"] = sender
        msg["To"] = ",".join(recipient)

        # 发送邮件
        try:
            s.sendmail(from_addr=sender, to_addrs=msg["To"].split(","), msg=msg.as_string())
            logging.info("发送邮件成功")
        except Exception as e:
            logging.info("发送邮件失败")
            raise e
        finally:
            s.quit()


if __name__ == '__main__':
    import os
    from common.constant import REPORT_DIR


    file_path = os.path.join(REPORT_DIR, "report.html")
    title = conf.get("email", "mail_title")
    message = conf.get("email", "mail_message")
    SendEmail.send_qq_file_email(title=title, message=message, file_path=file_path)






