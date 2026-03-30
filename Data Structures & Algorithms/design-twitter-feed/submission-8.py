class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followMap[userId].add(userId)

        if len(self.followMap[userId]) > 10:
            maxHeap = []
            for followee in self.followMap[userId]:
                if followee in self.tweets:
                    index = len(self.tweets[followee]) - 1
                    count, tweetId = self.tweets[followee][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followee, index - 1])
            
            while len(maxHeap) > 10:
                heapq.heappop(maxHeap)
            
            while maxHeap:
                count, tweetId, followee, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followee, index])
        else:
            for followee in self.followMap[userId]:
                if followee in self.tweets:
                    index = len(self.tweets[followee]) - 1
                    count, tweetId = self.tweets[followee][index]
                    heapq.heappush(minHeap, [count, tweetId, followee, index - 1])
            
        while len(res) < 10 and minHeap:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
