# coding=utf8
import smtplib
from email.mime.text import MIMEText

from loguru import logger


class MyEmail:

    def __init__(self):
        self.mail_host = "smtp.126.com"
        self.username = "zxdstud@126.com"
        self.password = "ZOQLFCJUERCVPIDM"
        self.sender_email = self.username
        self.receivers = ["1296753187@qq.com"]
        self.server = smtplib.SMTP_SSL(self.mail_host, 465)
        try:
            self.server.login(self.username, self.password)
            logger.info("邮箱登录成功!")
        except smtplib.SMTPException as e:
            logger.warning(e)
            logger.warning("邮箱登录失败!")

    def sendEmail(self, title, message):
        self.server.send(message)

    def testConnect(self):
        self.server.helo()
        res = self.server.ehlo()
        if res is not None:
            logger.info(res)
            logger.info("邮箱服务器连接成功!")
        else:
            logger.warning(res)
            logger.warning("邮箱服务器连接失败!")


if __name__ == '__main__':
    myEmail = MyEmail()
    myEmail.testConnect()
