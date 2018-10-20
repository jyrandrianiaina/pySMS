import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def sending_email(): 
    fromaddr = "mymonitor@yahoo.fr"
    toaddr = "mymail@mail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Check astreinte pour ce jour"
    body = "Please find below the check of the day. "
    msg.attach(MIMEText(body, 'plain'))
    filename = "allresponse.docx"
    attachment = open("allresponse.docx", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('myserver', 587)
    server.starttls()
    server.login(fromaddr, "mypassword)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

sending_email()
