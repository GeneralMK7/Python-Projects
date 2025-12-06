import smtplib
email = "lytblenders@gmail.com"
password = "wtch dlbs cusm lfxt"

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(email,password)
    connection.sendmail(from_addr= "lytblenders@gmail.com",
                        to_addrs= "madhukiran.golla.personal@gmail.com",
                        msg="Subject: Information regarding your new Internship\n\n"
                            "Hope this email finds you! Congrats on your first Internship")
