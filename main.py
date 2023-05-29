import random
import smtplib
import datetime as dt

MY_EMAIL = "doteflon319@gmail.com"
PASSWORD = "evgrvkvcrksgsfyi"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as Quote_file:
        all_quotes = Quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="teflonghost@yahoo.com",
            msg=f"Subject:Monday Motivation \n\n{quote}.")



