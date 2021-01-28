import datetime as dt
from pandas import *
from tkinter import messagebox
import smtplib

my_email = "przemassoprzemo@gmail.com"
email_to_send = "przemoszadkowski@o2.pl"
password = "Jonathan21#"

now = dt.datetime.now()
month = now.month
day = now.day

try:
    birthday_frame = pandas.read_csv('birthdays.csv')
except FileNotFoundError:
    messagebox.showinfo(title='Not found!', message="Birthday's data not found!")
else:
    birthday_dict = birthday_frame.to_dict(orient='records')
    for item in birthday_dict:
        if item['month'] == month and item['day'] == day:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email_to_send,
                    msg=f"Subject: Urodziny - przypomnienie!!\n\nToday's birthday - {item['name']}"
                )