#/usr/bin/env python

import argparse
import setplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

parser= argparse.ArgumentParser(description= "beacon info")
parser.add_argument('--computer')
parser.add_argument('--ip')
args = parser.parse_args()

fromaddr = "<gmail-account-here>"
toaddr = ["7777777@txt.att.net", "888888@text.com"]
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "Incoming BEACON"

hostname = args.computer
internal_ip= args.ip

body= "Check your server! \n Hostname: " + hostname+
" \nInternal IP:"+ internal_ip

msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com', S87)
server.starttls()
server.login(fromaddr, "<gmailPasswordHere>")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()