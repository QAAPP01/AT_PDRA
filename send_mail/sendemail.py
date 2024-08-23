import smtplib
import os
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename


def compress_attachments(attachment_list, zip_filename="attachments.zip"):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in attachment_list:
            zipf.write(f, basename(f))
    return zip_filename


def send_mail(opts):
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

    # Check the total size of attachments
    total_size = sum(os.path.getsize(f) for f in attachment)
    max_size = 25 * 1024 * 1024  # 25 MB

    if total_size > max_size:
        print(f"Attachments exceed {max_size / (1024 * 1024)} MB, compressing...")
        zip_file = compress_attachments(attachment)
        attachment = [zip_file]  # Replace with the zip file

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
