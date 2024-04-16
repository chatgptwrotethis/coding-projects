import random
import datetime
import smtplib
import pandas as pd
SENDER = "autobirthday32@gmail.com"
SENDER_PASSWORD = "bzrd kfvv tllb jgba"

data =  pd.read_csv("automated birthday wisher/birthdays.csv")
now = datetime.datetime.now()

for index,row in data.iterrows():
    if now.day == row.day and now.month == row.month:
        file_path = f"automated birthday wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            print(contents)
            
            contents = contents.replace("[NAME]", row.names)
            print(contents)

            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=SENDER, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER, to_addrs=row.email, msg=f"Subject: Happy Birthday!\n\n{contents}")
            connection.quit()

