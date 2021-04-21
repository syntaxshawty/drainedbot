# Twitter Bot Using Python and AWS Lambda

This is a simple template you can use to build a twitter bot that tweets fake lyrics from your favorite musician using web scraping, Markov Chaining, Python and an AWS Lambda Function. I used it to create [@dg_unreleased](https://twitter.com/dg_unreleased). This is adapted from Dylan Castillo's wonderful tutorial which you should check out [here.](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/)

## Pre-requisites

To build and use the bot, you'll need a few things:

1.  Register for a [twitter developer account](https://developer.twitter.com/en)
2.  Get [genius api keys](https://docs.genius.com/#/getting-started-h1)
3.  Generate genius access token
4.  Have [Docker](https://docs.docker.com/docker-for-mac/install/) installed
5.  Have Python 3.8 or higher installed
6.  Create a [twitter app](https://developer.twitter.com/en/portal/projects-and-apps)
7.  Make sure to give it **Read and Write** permissions.
8.  Set up an [AWS account](https://aws.amazon.com/)
9.  Create a [Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) for your bot
10. Create a [Lambda Layer](https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d) to use additional libraries in your Lambda Function

-you can do 8 and 9 later DEFINITELY read thru Dylan's tutorial on his site it does an excellent breakdown of the steps for deployment

## How to use

To make your own bot follow these steps:

1. Clone [this](https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda) repository on your local machine
2. Create a virtual environment in your project's root directory: `python3 -m venv venv && source venv/bin/activate`
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `.env` in the root directory of your project. Put your twitter App keys there:

```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<YOUR_ACCESS_TOKEN_SECRET_HERE>
CONSUMER_KEY=<YOUR_CONSUMER_KEY_HERE>
CONSUMER_SECRET=<YOUR_CONSUMER_SECRET_HERE>
```

5. edit `lyric_scrape.py` adding your genius access token where it says YOUR-TOKEN-HERE
6. modify `lyric_scrape.py` to get your fave musicians lyrics by changing the artist name and song count on the last line in the file
7. run `lyric_scrape.py` to produce a txt file with all the scraped lyrics. You will want to get a lot of songs so you have diversity in the lyrics.
8. once you have the lyrics copy and paste them into the src/lyrics.txt file replacing the lyrics already there.
9. Test your changes locally by running `python entrypoint.py` from the root directory of your project

## How to deploy

Once you are happy with your bot:

[time to look at Dylan's walkthru deployment!](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/)

1. Add any additional packages you used to `requirements.txt`
2. Run `sh createlambdalayer.sh` from the root directory of your project. It'll generate a zip file with your libraries called `layer.zip` this will take a while!
3. Create a Lambda Layer by uploading the generated `layer.zip`
4. Run `sh buildpackage.sh` from the root directory of your project. It'll make a zip file with the code for your Lambda Function called `lambda_function.zip`
5. Create a lambda function by uploading `lambda_function.zip`
6. Add your twitter App keys as environment variables in the Lambda Function
7. Add a scheduled trigger to your Lambda Function using [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/run-lambda-schedule.html)

## Attributions

The `createlambdalayer.sh` script comes from [this repository](https://github.com/aws-samples/aws-lambda-layer-create-script).
