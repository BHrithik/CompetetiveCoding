class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize != 0:
            return False
        hand.sort()
        handCounter = Counter(hand)
        n = len(hand)
        for i in range(n//groupSize):
            cur = sorted(handCounter.keys())[0]
            for j in range(0,groupSize):
                if cur+j in handCounter:
                    handCounter[cur+j] -= 1
                    if handCounter[cur+j] == 0:
                        del handCounter[cur+j]
                else:
                    return False
        return True