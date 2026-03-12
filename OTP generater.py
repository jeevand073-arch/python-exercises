import random

def otp_generate():
    #to get 6digit number
    OTP = random.randint(100000,999999)
    return OTP
generatored = otp_generate()
print(generatored)
