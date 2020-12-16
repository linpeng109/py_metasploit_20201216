import smtplib
from email.header import Header
from email.mime.text import MIMEText


class QMail:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def sendMail(self):
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器，qq的SMTP服务host
        mail_user = "1911097168@qq.com"  # 用户名（须修改）
        mail_pass = "muerlqnrypihecif"  # 此处为在qq开启SMTP服务时返回的密码 （须修改）

        sender = '1911097168@qq.com'  # 同用户名 （须修改）
        receivers = ['1791776426@qq.com',
                     'linpeng109@aliyun.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        message = MIMEText('...', 'plain', 'utf-8')
        message['From'] = Header("python测试邮件", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        try:
            subject = 'Python SMTP 邮件测试'
            message['Subject'] = Header(subject, 'utf-8')
            smtpObj = smtplib.SMTP(host=mail_host)
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.ehlo()
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as error:
            print(error)
            print("Error: 无法发送邮件")


if __name__ == '__main__':
    robot = QMail()
    robot.sendMail()
