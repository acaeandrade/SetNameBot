from charset_normalizer import api
import tweepy

def Autenticação():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    #Login a partir das chaves
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #Declaração para chamar a api sem espamar
    Api = tweepy.API(auth, wait_on_rate_limit=True)