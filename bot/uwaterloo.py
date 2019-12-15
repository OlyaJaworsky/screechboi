# Print out `limit` submissions from the subreddit 'uwaterloo'.
def hot(reddit, limit = 10):
    # For every 'submission' (a variable) in the subreddit 'uwaterloo', print
    # out its title.
    for submission in reddit.subreddit('uwaterloo').hot(limit=limit):
        print(submission.title)