import yagmail
import pandas
from news import NewsFeed
import datetime
import time


while True:
    if datetime.datetime.now().hour == 00 and datetime.datetime.now().minute == 19:
        df = pandas.read_excel('people.xlsx')
        for index, row in df.iterrows():
            from_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            to_date = datetime.datetime.now().strftime('%y-%m-%d')
            news_feed = NewsFeed(interest=row['interest'], from_date=from_date, to_date=to_date)
            email = yagmail.SMTP(user="pythondjango276@gmail.com", password="Hello@World123")
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today!",
                       contents=f"Hi {row['name']},\nSee what's on about {row['interest']} today.\n\n{news_feed.get()}\nPython Django")

    time.sleep(60)
