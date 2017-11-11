import tweepy

def get_configuration(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def start_tweet():

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    api = get_configuration(consumer_key, consumer_secret, access_token, access_token_secret)
    file = open('random_words.txt', 'rU')

    for line in file:
        status = api.update_status(status=line)
        print 'Success!'

if __name__ ==  "__main__":
    start_tweet()
