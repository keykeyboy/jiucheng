# python  发送html邮件
# smtp:是一种简单的邮件传输协议
# smtplib:封装了smtp协议,所以对于邮件发送就更加简单了
import smtplib
# 文本方法
from email.mime.text import MIMEText
# 设置头部内容
from email.header import Header

# user = '718605327@qq.com'
# password = 'bxwgayvokxrbbaie'
# 创建邮箱服务器连接 smtplib.SMTP_SSL(邮箱连接地址,端口号)smtp.xx.com  端口号  ssl  465 587  邮局
# 邮箱163:smtp.163.com
# qq邮箱:smtp.qq.com
class Email_Send:
    def email_html(self,htmlContent):
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
        # htmlContent = '''
        #     <!doctype html><!--声明当前文档类型-->
        # <html><!--网页结构的开始--->
        # 	<head><!--描述网页基本信息-->
        # 		<meta charset="UTF-8"><!--声明网页编码格式-->
        # 		<meta name="Keywords" content="关键字,关键词">
        # 		<meta name="Description" content="描述和简介">
        # 		<title></title>
        #
        # 	</head>
        # 	<body><!--可视区域-->
        # 		</p>html主题</p>
        # 		<h1>标题标签</h1>
        # 	</body>
        # </html>
        # '''

        # 准备发送邮件  _text 邮件正文  _subtype 文件类型  文本  html  base64(二进制类型)  plain默认就是纯文本  _charset 编码格式
        message = MIMEText(_text=htmlContent, _subtype='html', _charset='utf-8')

        # 设置头部内容
        # 设置头部标题
        message['Subject'] = Header('文本标题', 'utf-8')
        # 发件人
        message['From'] = Header('<718605327@qq.com>', 'utf-8')
        # 收件人
        message['To'] = Header('<718605327@qq.com>', 'utf-8')

        # 发送邮件
        con.sendmail(sender, recevier, message.as_string())


if __name__ == '__main__':
    Email_Send().email_html('1111')
