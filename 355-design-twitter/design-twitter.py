class Twitter:

    def __init__(self):
        self.post_map = {}
        self.follow_map = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post_map:
            self.post_map[userId] = []
        self.post_map[userId].append([-self.time,tweetId])
        self.time += 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = self.follow_map[userId] if userId in self.follow_map else set()
        ids.add(userId)
        all_posts = []
        res = []
        for id in ids:
            if id in self.post_map and self.post_map[id]:
                posts = self.post_map[id]
                index = len(posts)-1
                time, tweetId = posts[index]
                all_posts.append([time, id, tweetId,index-1])
        heapq.heapify(all_posts)
        while all_posts and len(res) < 10:
            time, id, tweetId, index = heapq.heappop(all_posts)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.post_map[id][index]
                heapq.heappush(all_posts,[time, id, tweetId, index-1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()
        self.follow_map[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].remove(followeeId)
        return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)