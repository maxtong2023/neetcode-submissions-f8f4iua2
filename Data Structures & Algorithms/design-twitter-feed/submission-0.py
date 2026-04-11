import heapq

class Twitter:

    def __init__(self):
        # needs a follow list mapping every userid to a list of user id's that
        # they are following. Hashmap.

        # needs another data structure representing all of the tweets. 
        # I think i can make this a tuple with the first element being the 
        # tweet id and the second element being the user id? 

        self.followings = {}
        self.tweets = []
        self.tweetindex = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        # tweets at the start of the list are the ones that are more recent. 
        heapq.heappush(self.tweets, (-self.tweetindex, userId, tweetId))
        self.tweetindex +=1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed=[]
        copy = self.tweets[:]
        user_follows = self.followings.get(userId, set())
        while len(feed) < 10 and copy: 
            neg_idx, t_user_id, t_id = heapq.heappop(copy)
            if t_user_id == userId or t_user_id in user_follows: 
                feed.append(t_id)
        return feed



        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followings:
            self.followings[followerId] = set()
        self.followings[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followings:
            self.followings[followerId].discard(followeeId)

        
