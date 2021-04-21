import os
import random
import json
from pathlib import Path
import tweepy
import csv
import markovify
import re
import spacy

ROOT = Path(__file__).resolve().parents[0]

nlp = spacy.load("en_core_web_sm")

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


with open("./src/lyrics.txt") as f:
    text = f.read()

def write_lyric(origin_file):
    text_model = markovify.NewlineText(text, state_size=2)
    lyric = ''
    for i in range(4):
        lyric += text_model.make_short_sentence(70, max_overlap_ratio=0.5, tries=100)
        lyric += '\n'
    return lyric

def lambda_handler(event, context):
    print("Getting credentials...")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticating...")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Getting lyric to tweet")
    tweet = write_lyric(text)

    print(f"Post tweet: {tweet}")
    api.update_status(tweet)

    return {"statusCode": 200, "tweet": tweet}
