import datetime as dt
import smtplib as smtp
import pandas as pd
import random
import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path("Automatic Email Wisher\.env")
load_dotenv(env_path)

now=dt.datetime.now()
print(now.date())

username=os.getenv("EMAIL1")
g_password= os.getenv("PASSWORD1")
print(username,g_password)

df= pd.read_csv(r"Automatic Email Wisher\files\birthdays.csv")

df_len=len(df)
df_dict={}

def count_age(y,m,d):
    if ((now.month,now.day)>=(m,d)):
        age=now.year-y
    else:
        age=now.year-y-1
    return age

today=f"{now.month :02}-{now.day :02}"

def message_gen():
    a=random.randint(1,3)
    f=f"letter_{a}.txt"
    with open(f"letter_templates\\{f}","r") as file:
        message=file.read()
        return message

with smtp.SMTP("smtp.gmail.com",587) as server:
    server.starttls()
    server.login(user=username,password=g_password)
    for n in range(0, df_len):
        a=df.loc[n]
        age=count_age(y=a["year"],m=a["month"],d=a["day"])
        name=a["name"]
        day=f"{a["month"] :02}-{int(a["day"]):02}"
        if (today == day):
            message=message_gen()
            message=message.replace("[NAME]",name)
            server.sendmail(from_addr=username,to_addrs=a["email"],msg=f"Subject:Happy Birthday to My Dear {name} \n\n {message}")
            print(message)
