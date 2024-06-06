class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize != 0:
            return False
        hand.sort()
        n = len(hand)
        for i in range(n//groupSize):
            cur = hand[0]
            for j in range(0,groupSize):
                if cur+j in hand:
                    hand.pop(hand.index(cur+j))
                else:
                    return False
        return True