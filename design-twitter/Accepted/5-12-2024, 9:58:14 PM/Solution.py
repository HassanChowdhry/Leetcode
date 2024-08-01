// https://leetcode.com/problems/design-twitter

class Twitter:

    def __init__(self):
        self.k = 10
        self.user_posts = {}
        self.user_follow = {}
        self.post_occurence = {}
        self.postId = 0
        self.tweeId_check = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_posts:
            self.user_posts[userId] = []
        if tweetId not in self.tweeId_check:
            self.tweeId_check.add(tweetId)
            self.post_occurence[self.postId] = tweetId
        if self.postId not in self.user_posts[userId]:
            self.user_posts[userId].append(self.postId)
        
        self.postId += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heapq.heapify(heap)

        if userId in self.user_posts:
            for vals in self.user_posts[userId]:
                if len(heap) >= self.k:
                    heapq.heappop(heap)
                heapq.heappush(heap, vals)

        if userId not in self.user_follow:
            res = sorted(heap, reverse=True)
            res = [self.post_occurence[num] for num in res]
            return res
        
        followers = self.user_follow[userId]

        for follow in followers:
            if follow not in self.user_posts:
                continue 

            posts = self.user_posts[follow]
            for post in posts:
                if len(heap) >= self.k:
                    heapq.heappop(heap)
                heapq.heappush(heap, post)

        res = sorted(heap, reverse=True)
        res = [self.post_occurence[num] for num in res]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follow:
            self.user_follow[followerId] = []

        if followeeId not in self.user_follow[followerId]:
            self.user_follow[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_follow:
            if followeeId in self.user_follow[followerId]:
                self.user_follow[followerId].remove(followeeId)
        
            if len(self.user_follow[followerId])==0:
                del self.user_follow[followerId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)