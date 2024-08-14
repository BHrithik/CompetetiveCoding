class Twitter:

    def __init__(self):
        self.feed = deque() 
        self.followers = defaultdict(lambda: set())
        self.tweets = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        count = 0
        feed = []
        following = self.followers[userId]
        following.add(userId)
        for id,tweet in self.tweets:
            if id in following:
                feed.append(tweet)
            if len(feed)==10:
                break
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)