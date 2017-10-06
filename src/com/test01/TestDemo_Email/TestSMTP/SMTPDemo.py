# -*- coding:utf8 -*-
"""
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件

"""
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = '948906782@qq.com'
password = 'ulvcfeudzwjabfjc'
# 输入收件人地址:
to_addr = '1241625444@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 夹带附件形式-
"""
同时支持HTML和Plain格式

如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？

办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。

利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative

msg = MIMEMultipart('alternative')
.
.
.
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
"""
msg=MIMEMultipart()
msg['From']=_format_addr(from_addr)
msg['To']=_format_addr(to_addr)
msg['Subject']=Header('Come from SMTP....','utf-8').encode()
msg.attach(MIMEText("send with field",'plain','utf-8'))
with open('J:/a.jpg','rb') as f:
    mine=MIMEBase('image','jpg',filename='a.jpg')
    mine.add_header('Content-Disposition', 'attachment', filename='a.jpg')
    mine.add_header('Content-ID', '<0>')
    mine.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mine.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mine)
    # 添加到MIMEMultipart:
    msg.attach(mine)
#发送文本形式-
# msg=MIMEText('hello,send by Python...','plain','utf-8')
"""发送板块"""
import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

