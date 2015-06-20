from data import load_tweets

def most_talkative_state(tweets,find_state):
    """Return the state that has the largest number of tweets containing term.
    """

    state = []
    #create a list of all tweets locations
    for index in range(len(tweets)):
        state.append(find_state(tweets[index]))
    if len(state) == 0:
        return
    #return the state the appear the most on the list we built using key in
    # max (the max value relevant to the count)
    return max(state, key = state.count)



def average_sentiments(tweets_by_state,word_sentiments):
    """Calculate the average sentiment of the states by averaging over all
    the tweets from each state. Return the result as a dictionary from state
    names to average sentiment values (numbers).

    If a state has no tweets with sentiment values, leave it out of the
    dictionary entirely.  Do NOT include states with no tweets, or with tweets
    that have no sentiment, as 0.  0 represents neutral sentiment, not unknown
    sentiment.

    tweets_by_state -- A dictionary from state names to lists of tweets
    """
    sentimentDict = {}
    for state,tweets in tweets_by_state.items():
        summarizeSentiment = 0
        numOfCountedTweets = 0
        for index in range(len(tweets)):
            #if we got value from 'get_sentiment' func, sum it and add 1 to
            # the counter (that count how many tweets we summarized
            if tweets[index].get_sentiment(word_sentiments) != None:
               summarizeSentiment += \
                   tweets[index].get_sentiment(word_sentiments)
               numOfCountedTweets += 1
            #if we summarized, update the dictionary with value - state,
            # key - average
            if numOfCountedTweets != 0:
                sentimentDict.update({state : summarizeSentiment
                / numOfCountedTweets})
    return sentimentDict


def group_tweets_by_hour(tweets):
    """Return a list of lists of tweets that are gouped by the hour 
    they were posted.

    The indexes of the returned list represent the hour when they were posted
    - the integers 0 through 23.

    tweets_by_hour[i] is the list of all
    tweets that were posted between hour i and hour i + 1. Hour 0 refers to
    midnight, while hour 23 refers to 11:00PM.

    To get started, read the Python Library documentation for datetime 
    objects:
    http://docs.python.org/py3k/library/datetime.html#datetime.datetime

    tweets -- A list of tweets to be grouped
    """
    llistOfLists = [[] for hour in range(24)] #create list of 24 lists inside
    for index in range(len(tweets)):
        time = tweets[index].get_time()
        #enter tweet in the hour it posted (using .hour that represent the
        # hour of 'datetime' class from 0 to 23 (just like list index))
        llistOfLists[time.hour].append(tweets[index])
    return llistOfLists
