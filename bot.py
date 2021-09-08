import tweepy
import time

CONSUMER_KEY = 'INSIRA A KEY ESPECIFICA AQUI'
CONSUMER_SECRET = 'INSIRA A KEY ESPECIFICA AQUI'
ACCESS_TOKEN = 'INSIRA A KEY ESPECIFICA AQUI'
ACCESS_TOKEN_SECRET = 'INSIRA A KEY ESPECIFICA AQUI'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#Pasta onde os ID's dos tweets já respondidos vão, para que o bot não fique respondendo os mesmos tweets repetidamente
FILE_NAME = 'botTwitter\last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def responder():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        #Hashtag que o vai ler para responder o tweet
        if '#testbotjoac' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            #Mensagem que você deseja que ele escreva ao responder
            api.update_status("@" + tweet.user.screen_name + " Resposta, like e retweet automatica esta funcionando", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    responder()
    time.sleep(2)
