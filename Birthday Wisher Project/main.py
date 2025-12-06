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
date_of_all = birthday_file["day"].to_list()
month_of_all = birthday_file["month"].to_list()

for i in range(len(date_of_all)):
    if date_of_all[i] == date and month_of_all[i] == month:
        info = birthday_file[birthday_file["day"] == date_of_all[i]]
        for index,row in info.iterrows():
            send_email(row)
        break






