# OTP Verification System in Python

This repository contains a simple Python script to generate and verify a One Time Password (OTP) via email. The script uses the `smtplib` library to send the OTP to a specified email address and validates the input OTP against the generated one.

## Features

- Generates a random 6-digit OTP.
- Sends the OTP to the user's email address using Gmail's SMTP server.
- Verifies the user-inputted OTP.

## Prerequisites

- Python 3.x
- Gmail account with "App Password" enabled. Follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en) to generate an App Password.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/otp-verification-system.git
   cd otp-verification-system
   ```

2. Install necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Open the `otp_verification.py` file and replace the placeholders with your Gmail account and App Password:
   ```python
   s.login("Your Gmail Account", "Your App Password")
   ```

2. Run the script:
   ```sh
   python otp_verification.py
   ```

3. Enter your email address when prompted, and then check your email for the OTP.

4. Enter the OTP received in the email to verify.

## Code Overview

```python
import math
import random
import smtplib

# Generate a 6-digit OTP
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp_msg = OTP + " is your One Time Password"
msg = otp_msg

# Configure SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# Login to your Gmail account
s.login("Your Gmail Account", "Your App Password")

# Get the user's email address
emailid = input("Please enter your Email: ")
s.sendmail('Your Gmail Account', emailid, msg)

# Get the OTP from the user
a = input("Please enter the One Time Password sent to your email: ")

# Verify the OTP
if a == OTP:
    print("Your OTP is verified!")
else:
    print("Wrong OTP, please check it again")
```

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
