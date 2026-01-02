# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_my_birth = dt.datetime(year=2000, month=1, day=1)
# print(date_of_my_birth)
#------------------------------------------------------------------------------------
import smtplib
import datetime as dt
import random as rd

my_email = "mxm.0000001@gmail.com"
with open(file="./password.txt", mode='r') as f:
    password = f.read()

with open(file="quotes.txt", mode='r') as f:
    quotes = f.readlines()

now = dt.datetime.now()
if now.weekday() == 4: #if the day of the week is friday
    quote_of_the_day = rd.choice(quotes)
    print("Subject:Happy Friday!\n\n" + quote_of_the_day)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mxm.0000002@yahoo.com",
            msg="Subject:Happy Friday!\n\n" + quote_of_the_day
        )
