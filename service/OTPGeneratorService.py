import math
import random
class OTPGeneratorService:
    _instance = None
    def __init__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return

    def generateOTP(self):
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]
        return OTP
