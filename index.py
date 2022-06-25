import snscrape.modules.twitter as scrapper
import pandas as pd
import datetime

tweets = []
news_usernames = ["htTweets", "IndianExpress", "dna", "EconomicTimes"]

print("Initiating Twitter Scapper...")
for username in news_usernames:
    print(f"Fetching latest Tweets for @{username} ...")
    all_tweets = []
    for i, tweet in enumerate(scrapper.TwitterSearchScraper("from:"+username).get_items()):
        if i>100:
            break
        all_tweets.append([tweet.id, str(tweet.date).split("+")[0].strip(), tweet.content, tweet.user.displayname, tweet.url, tweet.likeCount])
    tweets.extend(sorted(all_tweets, key=lambda x: x[-1], reverse=True)[:10])
    print(f"Adding Top 10 most liked tweets by @{username} ...", end="\n\n")


tweets_df = pd.DataFrame(tweets, columns=["ID", "DateTime", "News", "Source", "Tweet Url", "Likes"])

print("Exporting all the Data as news.csv ...")
tweets_df.to_csv("news.csv", sep=",")
