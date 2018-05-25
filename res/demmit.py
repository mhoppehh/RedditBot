import praw

reddit = praw.Reddit(client_id		=	'9j5EqtXSNSlfwA',
                     client_secret	=	'I2_I2I8DXbJIoRJmzD3-tu0GygE',
                     user_agent		=	'windows:github.com/mhoppehh/RedditBot:v0.0.1 (by /u/polyurethanes)')

subreddit = reddit.subreddit("politics")

f= open("data.csv","w+")
f.write("Title,URL,Score\n")

for submission in subreddit.top('year'):
    print("Title: ", submission.title)
    print("URL: ", submission.url)
    print("Score: ", submission.score)
    print("---------------------------------\n")
    f.write('{},{},{:d}\n'.format(submission.title.replace(',',''),submission.url,submission.score))
	
f.close()