import praw
import time

# Made by /u/DiamondxCrafting.

try:
    reddit = praw.Reddit(client_id='', client_secret='',
                         username='', password='',
                         user_agent='')
except Exception as e:
    print("#Login failed.", e)


try:
    open('postid.txt', 'r')
except FileNotFoundError:
    open('postid.txt', 'w')


# Check if the submission id is in the postid list.
def postidcheck(postid):
    postidlist = open('postid.txt', 'r+').read().split('\n')
    for post in postidlist:
        if postid == post:
            return post
            break


sublist = ["test"]  # Subreddit list to crosspost to.
privatesub = 'privatesub'  # Subreddit to crosspost from.
privatesub = reddit.subreddit(privatesub)

while True:
    for submission in privatesub.new(limit=None):
        if submission.id == postidcheck(submission.id):  # Check if the submission has already been crossposted.
            continue
        for sub in sublist:  # Go through each each subreddit in the sublist.
            try:
                submission.crosspost(sub)  # Crosspost the submission in the current subreddit.
                open('postid.txt', 'a+').write(f'{submission.id}\n')  # Add the submission's id to the list.
            except Exception as e:
                print(e)
            time.sleep(600)  # 10 minutes cooldown due to reddit's ratelimit.
