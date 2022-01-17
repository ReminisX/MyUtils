import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 日志记录
from loguru import logger


class MyEmail:

    def __init__(self):
        """
        初始化服务
        """
        # SMTP服务器域名
        self.host = "smtp.126.com"
        # 发送者
        self.sender = "zxdstudy@126.com"
        # 授权码
        self.licence = "LHSQCIETJEOVFDQT"
        # 收件人
        self.receivers = ["1296753187@qq.com", "329772543@qq.com"]
        self.server = smtplib.SMTP_SSL(self.host, 465)
        try:
            self.server.login(self.sender, self.licence)
            logger.info("邮箱登录成功!")
        except smtplib.SMTPException as e:
            logger.warning(e)
            logger.warning("邮箱登录失败!")

    def writeEmail(self):
        """
        构建邮件内容主体
        :return:
        """
        # 构建邮件对象
        emali = MIMEMultipart('related')
        # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
        emali["From"] = "晓东<zxdstudy@126.com>"
        # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
        emali["To"] = "东<1296753187@qq.com>, 大东<329772543@qq.com>"
        # 设置邮件主题
        email["Subject"] = Header("""Python邮件测试""", 'utf-8')

        # 邮件正文内容
        body_content = """你好，这是一个测试邮件！"""
        # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
        message_text = MIMEText(body_content, "plain", "utf-8")
        # 向MIMEMultipart对象中添加文本对象
        email.attach(message_text)

        # 添加图片
        with open("static/photo/坚果.jpg", 'rb') as f:
            emali.attach(MIMEImage(f.read()))

        # 添加附件
        with open("static/file/附件工作表.xlsx", 'rb') as f:
            atta = MIMEText(f.read(), 'base64', 'utf-8')
            atta["Content-Disposition"] = 'attachment; filename="sample.xlsx"'
            emali.attach(atta)

        return emali

    def sendEmail(self, emali):
        self.server.sendmail(self.sender, self.receivers, email)

    def sendEmailSimple(self, message):
        message = message.encode('utf-8')
        try:
            self.server.send(message)
            logger.info("邮件发送成功")
        except smtplib.SMTPException as e:
            logger.warning("邮件发送失败")
            logger.warning(e)

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
    myEmail.sendEmail("你好啊")
