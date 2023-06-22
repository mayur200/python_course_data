import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import smtplib
password = 'xlfttgxwklmesvaa'
# me == my email address
# you == recipient's email address


# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

email_sender = "mayurpardeshi7@gmail.com"
email_password = password

email_receiver = "xecosax354@oniecan.com"

subject = "Dont forget to 2"
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.

em  = EmailMessage()
em['From'] =email_sender
em['To'] = email_receiver
em['Subject'] = subject
# em.set_content(body)

# em.attach(part1)
em.attach(part2)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
