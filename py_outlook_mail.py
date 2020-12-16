import smtplib


class OutlookMail:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def sendMail(self, message):
        mail_host = self.config.get('outlook', 'mail_host')
        mail_port = self.config.getint('outlook', 'mail_port')
        mail_ssl_port = self.config.getint('outlook', 'mail_ssl_port')
        mail_user = 'goldenhello1900@outlook.com'
        mail_password = self.config.get('outlook', 'mail_password')

        sender = self.config.get('outlook', 'sender')
        receivers = self.config.get('outlook', 'receivers').split(';')

        try:
            smtpObj = smtplib.SMTP(host=mail_host, port=mail_port)
            self.logger.debug('send mail success')
        except Exception as error:
            self.logger.error(error)
            smtpObj = smtplib.SMTP_SSL(host=mail_host, port=mail_ssl_port)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(user=mail_user, password=mail_password)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()


# try:
#     smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
# except Exception as e:
#     print(e)
#     smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
# # type(smtpObj)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login('goldenhello1900@outlook.com', '1qaz2wsx3edc')
# smtpObj.sendmail('goldenhello1900@outlook.com', 'goldenhello1900@outlook.com', body)  # Or recipient@outlook
#
# smtpObj.quit()
if __name__ == '__main__':
    outlook = OutlookMail()
    outlook.sendMail()
