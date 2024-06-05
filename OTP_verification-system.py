'''Steps to create an OTP verification system using python'''
# 1. Firstly we will design random 6 digit code number
# 2. Than we will store this number to a varaiable
# 3. then we need to write a program to send the email
# 4. when sending an email, we need to use the OTP as a message
# 5. Finally we need to request 2 user input, first for the user's email and then for the OTP that the user has received

import math
import os #operating system
import maths #maths module
import random #random module
import smtplib #Simple Mail Transfer Protocol library

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
    otp = OTP + " is your One Time Password"
    msg = otp

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
# this link is for singing the google app password. please foloow the instruction : https://support.google.com/accounts/answer/185833?hl=en

    s.login("Your Gmail Account", "Your App Password(16-digit)")
    emailid = input("Please enter your Email: ")
    s.sendmail('&&&&&&&&&&&', emailid, msg)
    a = input("Please enter One Time Password send on your mail>> : ")
    if a == OTP:
        print("Your OTP is verified!")
    else:
        print("Wrong OTP, please check it again")
    