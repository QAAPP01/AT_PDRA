import smtplib
import os
import zipfile
import traceback

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename


def send_mail(opts):
    try:
        # Set info
        fileRead = lambda fileName, mode="r": open(os.path.dirname(__file__) + "//" + fileName, mode)
        me = opts['account']
        you = opts['to']
        password = opts['password']

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = opts['subject']
        msg['From'] = opts['from']
        msg['To'] = str(you)

        # Message data info
        text = opts['text']
        html = opts['html']
        attachment = opts['attachment']

        # Transfer data
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html', 'utf-8')

        # Attach data into message container
        msg.attach(part1)
        msg.attach(part2)

        for f in attachment:
            with open(f, "rb") as fil:
                part = MIMEApplication(fil.read(), Name=basename(f))
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(me, password)
        mail.sendmail(me, you, msg.as_string())
        mail.quit()
    except Exception:
        traceback.print_exc()