import datetime as dt
import smtplib as smtp

with open(r"files\quotes.txt","r") as file:
    quote_list=[line.strip() for line in file.readlines()]

quote=random.choice(quote_list)
now= dt.datetime.now()
if (now.weekday() == 0):
    with smtp.SMTP("smtp.gmail.com",587) as server:
        username="xxxxxxx@gmail.com"
        g_password= "xxxx xxxx xxxx xxxx"
        server.starttls()
        print(f"Subject:Make your day the best\n \n {quote}")
        server.login(user=username, password=g_password)
        server.sendmail(to_addrs="xxxxx.com", from_addr=username,msg=f"Subject :Make your day the best\n\n {quote}" )
else:
    print("This is not a monday")