import datetime as dt
import random,smtplib

def send_email(message):
    email = "your-email-address"
    password = "your-app-password"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="madhukiran.golla.personal@gmail.com",
                            msg= "Subject:Motivational Quote for the day\n\n" + message)

def send_quote():
    with open("quotes.txt","r") as f:
        quotes = f.readlines()
        random_number = random.randint(1,len(quotes) - 1)
        quote_to_be_sent = quotes[random_number]
        send_email(quote_to_be_sent)

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 4:
    send_quote()

