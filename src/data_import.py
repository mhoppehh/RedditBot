import praw
import os

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~—“”‘’'''
file_path = os.path.abspath('../bin/data.csv')

def remove_punctuation(input):
    no_punct = ""
    for char in input:
        if char not in punctuations:
            no_punct = no_punct + char
    #print(input)
    #print(no_punct)
    return no_punct

reddit = praw.Reddit(client_id		=	'9j5EqtXSNSlfwA',
                     client_secret	=	'I2_I2I8DXbJIoRJmzD3-tu0GygE',
                     user_agent		=	'windows:github.com/mhoppehh/RedditBot:v0.0.1 (by /u/polyurethanes)')

def poll_reddit():
    subreddit = reddit.subreddit("politics")

    f= open(file_path,"w+")

    for submission in subreddit.top('month'):
        f.write('{},{},{:d}\n'.format(remove_punctuation(submission.title),submission.url,submission.score))

    f.close()