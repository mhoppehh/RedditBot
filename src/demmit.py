import praw

reddit = praw.Reddit(client_id		=	'9j5EqtXSNSlfwA',
                     client_secret	=	'I2_I2I8DXbJIoRJmzD3-tu0GygE',
                     user_agent		=	'windows:com.example.myredditapp:v0.0.1 (by /u/polyurethanes)')

#subreddit = reddit.subreddit("learnpython")

#for submission in subreddit.hot(limit=5):
#    print("Title: ", submission.title)
#    print("Text: ", submission.selftext)
#    print("Score: ", submission.score)
#    print("---------------------------------\n")