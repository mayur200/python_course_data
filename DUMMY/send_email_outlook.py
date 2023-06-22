
from pywin32 import win32com
from datetime import datetime
import os

outlook = win32.Dispatch('outlook.application')

from Office
 import Message

html_template =     """ 
            <html>
            <head>
                <title></title>
            </head>
            <body>
                    {}
            </body>
            </html>
        """

final_html_data = html_template.format(df.to_html(index=False))

o365_auth = ('sender_username@company_email.com','Password')
m = Message(auth=o365_auth)
m.setRecipients('receiver_username@company_email.com')
m.setSubject('Weekly report')
m.setBodyHTML(final)
m.sendMessage()