# Copyright (c) LearnBuildShare
# Simple OTP verification example using Python Tuple
# No functions are used here, as we are learning Tuple basics.

import random

otp = random.randint(100000, 999999)
otp_tuple = (otp,)
print("Generated OTP:", otp_tuple[0])

entered_otp = input("Enter the OTP: ")

if entered_otp == str(otp_tuple[0]):
    print("OTP verified successfully.")
else:
    print("OTP is incorrect.")
