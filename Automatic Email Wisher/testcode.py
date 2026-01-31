import smtplib as smtp
with open (r"files\emailpass.txt","r") as file:
    credentials=[line.strip() for line in file.readlines()]
    my_email=credentials[0]
    password=credentials[1]

with smtp.SMTP("smtp.gmail.com",587) as server:
    message='''This is not some spam, it is important thing to do there years and as we know we have to make some layoffs based on the current economic situation thats been happening with our company and the nation. 
    All we want is to make sure everyone is not new afddsdfdsfsdfs fected by our layoffs. Just emberace it with the notion of developing nation. Thank you'''
    server.starttls()
    server.login(user= my_email,password=password)
    server.sendmail(from_addr=my_email,to_addrs="xxxxxxxxx@gmail.com",msg = f"Subject: Testing python 2 \n\n{message}")


