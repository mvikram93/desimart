import re
import logging
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class EmailService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return

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

    def send_Email(toEmail_ID, qr_file_name, trip_id):
        fromaddr = ""
        try:
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toEmail_ID
            msg['Subject'] = f"Elite Parking Booking - Trip ID : {trip_id}"
            body = f"Elite Parking Booking - Trip ID : {trip_id}"
            print(f"Email - {msg['To']}")
            msg.attach(MIMEText(body, 'plain'))
            filename = f"data/{qr_file_name}.png"
            attachment = open(filename, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f"attachment; filename= {qr_file_name}.png")
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "ppkkfjntahoxwumm")
            text = msg.as_string()
            s.sendmail(fromaddr, toEmail_ID, text)
            s.quit()
            return 0
        except:
            raise Exception("Cannot send the email")
            return 1
