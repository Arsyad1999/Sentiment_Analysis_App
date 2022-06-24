
#KELAS : 6C
#NIM : 19090134
#NAMA : ARSYAD ABDILLAH


from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '8ymb7cHHBLvJ1CD3OoM2MQ3tp'
consumer_secret = 'VqLf794gDvyT9FxwZWJzpTnGZXtOGrTeWeR1HX0dz338NmivPU'

access_token = '1400964573482471426-ccqV5crflCK0unViF4t2u8gR9jeKKU'
access_token_secret = 'FjGWiElyoKoPsPFc8KY3TvaEMkA24iiJvEBdNle0WQFpi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()