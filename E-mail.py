import smtplib
import zmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2236350998@qq.com"  # 用户名
mail_pass = "wzkysionostydjeg"  # 口令

sender = '2236350998@qq.com'
receivers = ['jason13552648187@sina.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart()
message['From'] = Header('1', 'utf-8')  # 发送者

message['To'] = Header("测试", 'utf-8')  # 接收者
subject = '测试邮件'
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText('邮件发送测试……', 'plain', 'utf-8'))

att1 = MIMEText(r'D:\Python学习\python作业\计算机\计算器.html', 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="计算器.html"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print('Error: 无法发送邮件')

