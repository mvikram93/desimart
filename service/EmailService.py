import re
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class EmailService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Email Service")

    def validate_email(email):
        # Regular expression for email validation
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return False

    # Function to Send Email
    def send_Email(self, toEmail_ID, orderID):
        toAddrs = [toEmail_ID, "groupmanager698@gmail.com"]
        for toAddr in toAddrs:
            fromAddr = "group4698@gmail.com"
            try:
                msg = MIMEMultipart()
                msg['From'] = fromAddr
                msg['To'] = toAddr
                msg['Subject'] = f'Order successfully placed: Order #{orderID}'
                body = "Dear Customer,\n\nWe're pleased to inform you that your order has been successfully placed. Thank you for choosing us!\n\nBest regards,\nThe Team"
                print(f"Email - {msg['To']}")
                msg.attach(MIMEText(body, 'plain'))
                #simple mail transfer protocol, port: 587
                smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
                #transport layer security
                smtp_obj.starttls()
                smtp_obj.login(fromAddr, "fqugmovkklkixxtv")
                text = msg.as_string()
                smtp_obj.sendmail(fromAddr, toEmail_ID, text)
                smtp_obj.quit()
            except:
                raise Exception("Cannot send the email")
                return 0
        return 1
