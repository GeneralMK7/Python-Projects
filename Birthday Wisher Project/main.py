import random,pandas
import datetime as dt
import smtplib
PLACEHOLDER = "[NAME]"

def send_email(birthday_person_data):
    email = "your-email-address"
    password = "your-app-password"
    name_of_person = birthday_person_data["name"]
    person_email = birthday_person_data["email"]
    with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt",mode='r') as template:
        content = template.read()
        new_content = content.replace(PLACEHOLDER, name_of_person)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs=person_email,
                            msg="Subject:Happy Birthday to You\n\n" + new_content)


today = dt.datetime.now()
date = today.day
month = today.month
birthday_file = pandas.read_csv('birthdays.csv')

# Filter for matching birthdays efficiently
matching_birthdays = birthday_file[(birthday_file["day"] == date) & (birthday_file["month"] == month)]

# Send emails for all matching birthdays
for index, row in matching_birthdays.iterrows():
    send_email(row)






