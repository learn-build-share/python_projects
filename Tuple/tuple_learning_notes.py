# Copyright (c) LearnBuildShare
# Tuple learning notes for beginners

# Definition:
# A Tuple is an ordered collection of values.
# It is immutable, meaning it cannot be changed after creation.

# Example 1: Create a tuple
otp_tuple = (123456,)
# `otp_tuple` stores one value in a tuple.

# Example 2: Access tuple value
print(otp_tuple[0])
# `[0]` accesses the first item inside the tuple.

# Example 3: Compare input with stored OTP
user_input = "123456"
# `user_input` stores the number typed by the user.

if user_input == str(otp_tuple[0]):
    # Compare the string input with the stored numeric OTP.
    print("OTP verified")
else:
    print("OTP not matched")

# Real-world analogy:
# Think of a bank sending an OTP to your phone.
# The OTP should stay fixed until the verification is complete.

# Interview-style answer:
# Why is Tuple used for OTP storage?
# Because Tuple is immutable, so the OTP value stays safe and unchanged during verification.
