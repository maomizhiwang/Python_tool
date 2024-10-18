import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

# 1. 配置邮箱信息
sender = 'xxxxxxxxxxxxxxxx'  # 发件人
receiver = 'xxxxxxxxxxx'  # 收件人
pass_code = 'xxxxxxxxxxxxxxxx'  # 授权码：是发件人的授权码，也就是你之前开启SMTP服务时返回的字符串

# 2. 邮箱服务连接
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)  # qq邮箱的smtp服务地址：smtp.qq.com，默认端口：25

# 3. 邮件内容的定义
text = '宝贝，下班没'  # 邮件正文
content = MIMEText(text, 'plain', 'utf-8')  # 实现邮件发送的内容定义，信封

# 4. 定义收件人与发件人，邮件主题等相关信息
content['From'] = formataddr(['普斯猫', sender])  # 设置发件人名称
content['To'] = Header(receiver, 'utf-8')  # 设置收件人名称
# 添加邮件的主体
email_theme = '宝贝'
content['Subject'] = Header(email_theme, 'utf-8')  # 实现邮件主题的添加。

# 5. 发送邮件
conn.login(sender, pass_code)  # 登录smtp服务，是用账号与授权码，而不是账号与密码。
conn.sendmail(sender, receiver, content.as_string())  # 邮件发送
print("发送成功")
# 6.关闭smtp服务
conn.close()
