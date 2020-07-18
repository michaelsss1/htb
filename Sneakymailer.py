from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_contacts(filename):
    emails = []
    names = []
    with open('maillist', 'r', encoding='utf-8') as contacts_file:
        for email in contacts_file:
            emails.append(email.strip())
            names.append(email.split("@")[0].strip())
        return names, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def sendmail():
    s = smtplib.SMTP(host = '10.10.10.197', port = 25)
    s.starttls()

names, emails = get_contacts("maillist.txt")
message_template = read_template("message.txt")

for sender in emails:
    for recipent in emails:
        for name in names:
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=name.title())
            if sender == recipent:
                break
            else:
                msg['From'] = sender
                msg['To'] = recipent
                msg['Subject'] = 'report'

                msg.attach(MIMEText(message, 'plain'))

                s.send_message(msg)
