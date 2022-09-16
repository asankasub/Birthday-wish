
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

my_email = "x" 
my_pass = "x"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(from_addr=my_email, to_adrss=email, msg=f"Subject: Happy Birthday!\n\n{letter}")
