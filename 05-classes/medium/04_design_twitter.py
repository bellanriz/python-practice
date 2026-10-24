"""
LeetCode 355 - Design Twitter

Design a simplified version of Twitter where users can post tweets,
follow/unfollow other users, and see the 10 most recent tweets in
their news feed.

Implement the Twitter class:
    - Twitter()                      -> Initializes the object.
    - post_tweet(userId, tweetId)    -> User posts a new tweet.
    - get_news_feed(userId)          -> Returns the 10 most recent
                                        tweet IDs in the user's feed.
                                        Each tweet must be posted by
                                        the user or someone they follow.
                                        Tweets are ordered from most
                                        to least recent.
    - follow(followerId, followeeId) -> The follower follows the followee.
    - unfollow(followerId, followeeId) -> The follower unfollows the followee.

Example:
    twitter = Twitter()
    twitter.post_tweet(1, 5)
    twitter.get_news_feed(1)         # -> [5]
    twitter.follow(1, 2)
    twitter.post_tweet(2, 6)
    twitter.get_news_feed(1)         # -> [6, 5]
    twitter.unfollow(1, 2)
    twitter.get_news_feed(1)         # -> [5]

Constraints:
    - 1 <= userId, followerId, followeeId <= 500
    - 0 <= tweetId <= 10^4
    - All tweet IDs are unique.
    - At most 3 * 10^4 calls total.

Hint: Use a global timestamp counter. For get_news_feed, use a
      min-heap to efficiently merge tweets from all followed users.
"""

import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        pass

    def post_tweet(self, userId: int, tweetId: int) -> None:
        pass

    def get_news_feed(self, userId: int) -> list[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


# Test cases
twitter = Twitter()
twitter.post_tweet(1, 5)
print(twitter.get_news_feed(1))   # Expected: [5]
twitter.follow(1, 2)
twitter.post_tweet(2, 6)
print(twitter.get_news_feed(1))   # Expected: [6, 5]
twitter.unfollow(1, 2)
print(twitter.get_news_feed(1))   # Expected: [5]
