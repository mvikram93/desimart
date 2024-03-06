import re
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',format='%(name)s - %(levelname)s - %(message)s')


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