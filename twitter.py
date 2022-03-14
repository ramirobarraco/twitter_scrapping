import configparser 
import tweepy as tw
import pandas as pd

config = configparser.RawConfigParser()
config.read(filenames = 'config.ini')

bearer_token = config['twitter']['BEARER_TOKEN']

api = tw.Client(bearer_token)
ids = {'CNNEE': 33884545,
 'todonoticias': 25992212,
 'clarincom': 8105922,
 'LANACION': 33989170,
 'infobaeamerica': 7827962}
tweets = {}
for id, value in ids.items():
    tweets[id] = api.get_users_tweets(value, max_results = 100, exclude = 'replies')

data = {}
data['journal'] = []
data['tweet'] = []
data['id'] = []
for id, news in tweets.items():
    for new in news.data:
        data['id'].append(new.id)
        data["journal"].append(id)
        data['tweet'].append(new.text)

df2 = pd.DataFrame(data)
df2 = df2.set_index('id')

df1 = pd.read_csv('news_twitter.csv')
df1 = df1.set_index('id')

df = pd.concat([df1,df2]).drop_duplicates()
print(df.shape)
df.to_csv('news_twitter.csv')


