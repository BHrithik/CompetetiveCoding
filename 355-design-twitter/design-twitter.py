from collections import defaultdict, deque
from typing import List

class Twitter:

    def __init__(self):
        self.feed = defaultdict(deque)  # Use a defaultdict to maintain feed per user
        self.followers = defaultdict(set)
        self.tweets = deque()  # Store all tweets
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))  # Add new tweets to the front of the deque
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # Collect tweets from the user's feed and their followees
        feed = []
        following = self.followers[userId]  # Get users whom the user follows
        following.add(userId)  # Add the user itself to the following set
        
        # Iterate through the tweets in reverse order (most recent first)
        for tweet_user, tweet_id in self.tweets:
            if tweet_user in following:
                feed.append(tweet_id)
                if len(feed) == 10:  # Return only the most recent 10 tweets
                    break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)