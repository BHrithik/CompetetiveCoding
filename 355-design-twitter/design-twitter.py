class Twitter:

    def __init__(self):
        self.posts = {}
        self.follow_dict = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append([-self.time,userId,tweetId])
        self.time += 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = self.follow_dict[userId] if userId in self.follow_dict else set()
        ids.add(userId)
        all_posts = []
        heapq.heapify(all_posts)
        for id in ids:
            user_posts = self.posts[id] if id in self.posts else []
            for time, userId, tweetId in user_posts:
                heapq.heappush(all_posts,[time,tweetId])
        new_posts = []
        while len(new_posts) < 10 and all_posts:
            new_posts.append(heapq.heappop(all_posts)[1])
        return new_posts



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_dict:
            self.follow_dict[followerId] = set()
        self.follow_dict[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_dict:
            self.follow_dict[followerId].remove(followeeId)
        return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)