# python  发送图片附件

# smtp:是一种简单的邮件传输协议
# smtplib:封装了smtp协议,所以对于邮件发送就更加简单了
# user = '718605327@qq.com'
# password = 'bxwgayvokxrbbaie'
import smtplib
# 文本方法
from email.mime.text import MIMEText

# 图片附件
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# 设置头部内容
from email.header import Header


class Email_Send:
    def email_photo(self,image_path):
        # 创建邮箱服务器连接 smtplib.SMTP_SSL(邮箱连接地址,端口号)smtp.xx.com  端口号  ssl  465 587  邮局
        # 邮箱163:smtp.163.com
        # qq邮箱:smtp.qq.com
        con = smtplib.SMTP_SSL('smtp.qq.com', '465')

        # 登录 用户名和密码
        # 163的用户名和密码,直接填写就行.如果说是qq的邮箱 用户名邮箱号,密码,授权密码 设置 --账户--开启POP3/SMTP服务--点击授权码
        con.login(user='718605327@qq.com', password='bxwgayvokxrbbaie')

        # 发送者账号
        sender = '718605327@qq.com'
        # 接收者账号
        recevier = ['718605327@qq.com']

        # 创建实例
        message = MIMEMultipart()

        message['From'] = Header('<718605327@qq.com>', 'utf-8')
        message['To'] = Header('<718605327@qq.com>', 'utf-8')
        message['Subject'] = Header('我是图片附件', 'utf-8')

        # 内容读取出来
        image1 = open(image_path, 'rb').read()
        # 内容放在附件中
        image_data = MIMEImage(image1)
        # 设置图片文件名
        image_data['Content-Disposition'] = 'attachment;filename="qq.jpg"'
        # 把附件放到邮件对象中
        message.attach(image_data)

        # 发送邮件
        con.sendmail(sender, recevier, message.as_string())

if __name__ == '__main__':
    Email_Send().email_photo('../photos/1.jpg')
