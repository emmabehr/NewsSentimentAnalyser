# nltk.download("vader_lexicon")
from urllib.request import urlopen, Request
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as pyplot
import pandas
import json

current_date = datetime.now()
past_date = current_date - timedelta(days=30)

configuration = {"api_key": ""}
try:
    config_file = open("api.conf")
    configuration = json.load(config_file)
except:
    print("")

newsapi = NewsApiClient(api_key=configuration["api_key"])

all_articles = newsapi.get_everything(q="astrazenica",
                                          language="en",
                                          sort_by="relevancy",
                                          from_param=past_date.strftime("%Y-%m-%d"),
                                          to=current_date.strftime("%Y-%m-%d")                                          
                                         )

articles = all_articles["articles"]
data = []
for article in articles:
    print(article)

    info = [article["publishedAt"],article["title"] + " " + article["description"]]
    data.append(info)

data_frame = pandas.DataFrame(data, columns=["publishedAt", "text"])

vader = SentimentIntensityAnalyzer()
calculate_news_score = lambda text: vader.polarity_scores(text)["compound"]
data_frame["news_score"] = data_frame["text"].apply(calculate_news_score)
data_frame["publishedAt"] = pandas.to_datetime(data_frame.publishedAt).dt.date

pyplot.figure(figsize=(10,12))
mean_data_frame = data_frame.groupby(["publishedAt"]).mean()
mean_data_frame = mean_data_frame.unstack()
mean_data_frame = mean_data_frame.xs("news_score").transpose()
mean_data_frame.plot(kind="line")

pyplot.show()