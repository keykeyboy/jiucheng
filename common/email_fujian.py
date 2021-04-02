# 发送附件邮件  txt文件,excel文件,pdf文件
import smtplib
# 发送附件
from email.mime.multipart import MIMEMultipart
# 文本
from email.mime.text import MIMEText
# 设置头部
from email.header import Header


class Email_Send:
    def email_fujian(self, file):
        con = smtplib.SMTP_SSL('smtp.qq.com', '465')
        con.login(user='718605327@qq.com', password='bxwgayvokxrbbaie')
        sender = '718605327@qq.com'
        recevier = '718605327@qq.com'

        # 发送附件
        # 实例化附件  创建了一个信封
        message = MIMEMultipart()
        # 文件在哪  rb 读files/test.txt
        content = open(file, 'rb').read()
        # 把读取出来的内容放在文本中 信纸
        file1 = MIMEText(content, 'base64', 'utf-8')
        # 信纸取个名字
        file1['Content-Disposition'] = 'attachment;filename="1.html"'
        # 把信纸放到信封中
        message.attach(file1)

        # 发送正文
        msg = MIMEText('我是附件正文', 'plain', 'utf-8')
        message.attach(msg)

        # 设置头部内容
        # 发件人
        message['From'] = Header('<718605327@qq.com>', 'utf-8')
        # 收件人
        message['To'] = Header('718605327@qq.com')
        # 标题
        message['Subject'] = Header('测试结果')
        # 发送邮件
        con.sendmail(sender, recevier, message.as_string())

if __name__ == '__main__':
    Email_Send().email_fujian('../webkeytest/demo/report/20210318_160214_report.html')
