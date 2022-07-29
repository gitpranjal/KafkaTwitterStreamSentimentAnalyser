# Importing Tweepy and time
import tweepy
import time

from kafka import KafkaConsumer, KafkaProducer

from sentiment_analyser import analSentiment

# Credentials (INSERT YOUR KEYS AND TOKENS IN THE STRINGS BELOW)
api_key = "43Aan54tvdNIwXpGzdx3AlOao"
api_secret = "fIueb8Qio5p1MxziZ8AwKY7HuBbzLvMPQZPqlk1LbX92YrhiHl"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAANI2fQEAAAAA16iXwPiZfkd7cm00WVTAwY0yaJ0%3Dm0ZvJ80VWBbmJbBShiy3np4I7o5rGoBRJvGCHO0QXuR4CqSR1U"
access_token = "797712826877898752-SciHPI1Nx4ouGvZ7ca0vdK9Sp2YktFT"
access_token_secret = "drxiqDttTIPBPoRFd7tXzYzdEO4n5BhEIqGIfDyzlU2k4"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

producer = KafkaProducer(bootstrap_servers="localhost:9092")
topicName = "Republicans"



# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):

        print("Connected")


    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            print(tweet.text)
            
            client.like(tweet.id)
            producer.send(topicName, str.encode(str(analSentiment(tweet.text))))

            # Delay between tweets
            time.sleep(1)
        

# Creating Stream object
stream = MyStream(bearer_token=bearer_token, wait_on_rate_limit=True)

# Adding terms to search rules
# It's important to know that these rules don't get deleted when you stop the
# program, so you'd need to use stream.get_rules() and stream.delete_rules()
# to change them, or you can use the optional parameter to stream.add_rules()
# called dry_run (set it to True, and the rules will get deleted after the bot
# stopped running).


print("#######")

for previousRule in stream.get_rules().data:
    stream.delete_rules(previousRule.id)






print(topicName)
rule = tweepy.StreamRule(topicName)
stream.add_rules(rule)


# Starting stream
#stream.filter(tweet_fields=["referenced_tweets"])
stream.filter()