class VideoSharingPlatform:

    def __init__(self):
        self.videoDict = defaultdict(lambda: {})
        self.count = 0
        self.freeIDs = set()
        self.nextID = 0

    def upload(self, video: str) -> int:
        if self.freeIDs:
            videoId = self.freeIDs.pop()  # Use an ID from the set of free IDs
        else:
            videoId = self.nextID  # Use the next available ID
            self.nextID += 1  # Increment the ID for the next video
        
        # Store the video information
        self.videoDict[videoId] = {"video": video, "views": 0, "likes": 0, "dislikes": 0}
        return videoId

    def remove(self, videoId: int) -> None:
        if videoId in self.videoDict:
            self.freeIDs.add(videoId)
            self.videoDict.pop(videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videoDict:
            return "-1"
        else:
            endMinute = min(endMinute, len(self.videoDict[videoId]["video"])-1)
            self.videoDict[videoId]["views"] += 1
            return self.videoDict[videoId]["video"][startMinute:endMinute+1]

    def like(self, videoId: int) -> None:
        if videoId in self.videoDict:
            self.videoDict[videoId]["likes"] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videoDict:
            self.videoDict[videoId]["dislikes"] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId in self.videoDict:
            return [self.videoDict[videoId]["likes"],self.videoDict[videoId]["dislikes"]]
        else:
            return [-1]

    def getViews(self, videoId: int) -> int:
        if videoId in self.videoDict:
            return self.videoDict[videoId]["views"]
        else:
            return -1


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)