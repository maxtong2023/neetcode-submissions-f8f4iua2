import heapq
from collections import defaultdict, deque


class Twitter:

    def __init__(self):
        # needs a follow list mapping every userid to a list of user id's that
        # they are following. Hashmap.

        # needs another data structure representing all of the tweets. 
        # I think i can make this a tuple with the first element being the 
        # tweet id and the second element being the user id? 

        self.followings = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.tweetindex = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        # tweets at the start of the list are the ones that are more recent. 
        self.tweetindex -= 1
        self.tweets[userId].appendleft((self.tweetindex, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed=[]
        userlist = self.followings[userId] | {userId}
        
        streams = []
        for i in userlist: 
            if i in self.tweets:
                streams.append(self.tweets[i])
        for time, tId in heapq.merge(*streams):
            feed.append(tId)
            if len(feed) == 10:
                break
        return feed




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followings:
            self.followings[followerId] = set()
        self.followings[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followings:
            self.followings[followerId].discard(followeeId)

        
