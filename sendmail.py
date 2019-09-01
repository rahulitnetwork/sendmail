#!/usr/bin/python3

# Author XYZ
import smtplib
import xlrd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#server settings - fixed part
s = smtplib.SMTP('smtp.gmail.com' , 587)
s.starttls()

# user and login info - fixed part
FROM = "rahulg@umbrellainfocare.com"
passd = "xchtphdqurkqozcr" #define app password here
s.login(FROM , passd)

#define subject and body - variable part
msg = MIMEMultipart()
msg['From'] = "Rahul Gupta"
msg['Subject'] = "Python Oops trainning notes"
BODY = """Hi Team,

Please refer to this URL for python basic oops concept.
URL: https://repl.it/@SomilAgarwal/KindlySnoopyDisc


Regards,
Rahul Gupta
Umbrellainfocare Pvt. Ltd.
M: 7042028777
E: rahulg@umbrellainfocare.com

"""

msg.attach(MIMEText(BODY, 'plain')) 

#email attachment 
filename = "aws.pdf"
attachment = open("aws.pdf", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p)

#email file database - variable part
floc = ("maildb.xlsx")

wb = xlrd.open_workbook(floc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

#email trigger - fixed part
for i in range(sheet.nrows):
    TO = str(sheet.cell_value(i,0))
    print("Email sending to: ", TO)
    msg['To'] = TO
    message = msg.as_string()
    #message = "From: %s\r\n" % SNAME + "To: %s\r\n" % TO + "Subject: %s\r\n" % SUBJECT + "\r\n" + text 
    s.sendmail(FROM, TO, message)

#server connection close
s.quit()

