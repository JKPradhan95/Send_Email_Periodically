

import yagmail
import os
import time
from datetime import datetime as dt

sender = 'senderdemo@gmail.com'
receiver = 'receiverdemo@gmail.com'

subject = 'This is the subject'

contents = """
Here is the content of the email
Hi!
"""

password = os.getenv('PASSWORD')
if not password:
    print("Error: PASSWORD environment variable not set.")
else:
    print("PASSWORD environment variable is set.")

try:
    while True:

        now = dt.now()
        if now.hour == 17 and now.minute == 5 :
            
            yag = yagmail.SMTP(user=sender, password=password)
            
            yag.send(to=receiver, subject=subject, contents=contents)
            print("Email Sent!")
            time.sleep(60)

except Exception as e:
    print(f"An error occurred: {e}")
