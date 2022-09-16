import smtplib
import datetime as dt
import random
import pandas as pd

##################### Extra Hard Starting Project ######################
now = dt.datetime.now()
month = now.month
year = now.year
day = now.day
df = pd.read_csv("C:/Users/Asanka/Desktop/Python Practice/Birthday Wisher (Day 32) start/birthdays.csv")
for index, row in df.iterrows():
    if row["year"] == year and row["month"] == month and row["day"] == day:
        name = row["name"]
        email = row["email"]        
        
letters = ['C:/Users/Asanka/Desktop/Python Practice/Birthday Wisher (Day 32) start/letter_templates/letter_1.txt',
'C:/Users/Asanka/Desktop/Python Practice/Birthday Wisher (Day 32) start/letter_templates/letter_2.txt',
'C:/Users/Asanka/Desktop/Python Practice/Birthday Wisher (Day 32) start/letter_templates/letter_3.txt']
chosen_letter = random.choice(letters)
with open(chosen_letter, 'r') as file:
    letter = file.read()
    letter = letter.replace("[NAME]", name)
with open(chosen_letter, 'w') as file:
    file.write(letter)

my_email = "x" 
my_pass = "x"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday!\n\n{letter}")

print(chosen_letter)




/home/asankasub/letter_templates/letter_1.txt


/home/asankasub/birthdays.csv


/home/asankasub/main.py
