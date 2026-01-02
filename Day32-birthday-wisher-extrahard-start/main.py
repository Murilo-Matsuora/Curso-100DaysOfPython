##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random as rd
import smtplib

SENDER_EMAIL = "mxm.0000001@gmail.com"
with open(file="password.txt", mode='r') as f:
    SENDER_PASSWORD = f.read()

birthdays_df = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
for row in birthdays_df.iterrows():
    if row[1]['month'] == now.month and row[1]['day'] == now.day:
        birthday_person_name = row[1]['name']
        birthday_person_email = row[1]['email']
        print(f"Happy Birthday to {birthday_person_name}!")

        chosen_template_number = rd.randint(1, 3)
        with open(file=f"letter_templates/letter_{chosen_template_number}.txt", mode='r') as f:
            letter = f.read()

        formatted_letter = letter.replace('[NAME]', str(birthday_person_name))
        print(formatted_letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_PASSWORD,
                to_addrs=birthday_person_email,
                msg=f"Subject:Automated Happy Birthday Message\n\n{formatted_letter}"
            )


