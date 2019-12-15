import praw  # import external library named "praw"

# Import pretrained "sentiment intensity analyzer".
from nltk.sentiment.vader import SentimentIntensityAnalyzer

bot_name = "screechboi"
lexicon_file = "lexicon.txt"


# This is the main function. It runs when this package is started as an
# excecutable.
def main():
    # Load PRAW configuration from 'praw.ini'.
    reddit = praw.Reddit(
        bot_name, user_agent=f"script:{bot_name}:0.0.1 (by /u/reewithme)",
    )

    # Initialize analyzer (instantiates the class).
    analyzer = SentimentIntensityAnalyzer(lexicon_file=lexicon_file)

    print("Streaming inbox items:")
    for message in reddit.inbox.stream(skip_existing=True):
        # Receive message.
        print(f">>> {message.author} <<<")
        print(message.body)
        print()

        # Analyze polarity.
        scores = analyzer.polarity_scores(message.body)  # returns a dict
        polarity = scores["compound"]  # get value for key 'compound' in dict
        print(f"[polarity]: {polarity}")
        print()

        # Select reply based on message polarity.
        if polarity > 0.5:
            reply = "OWO!!"
        elif polarity > 0:
            reply = "owo"
        elif polarity < -0.5:
            reply = "no-wo :(("
        else:
            reply = "ree"

        # Reply to message.
        print(f"<<< {bot_name} >>>")
        print("Replying with:")
        message.reply(reply)
        print(reply)
        print()


# If this package is being imported by another library, do nothing.
#
# However, if it is being run as an executable, run the 'main' function.
if __name__ == "__main__":
    main()
