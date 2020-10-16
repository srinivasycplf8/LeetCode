class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand)%W !=0:
            return False

        counts={}
        hand.sort()
        for i in range(len(hand)):
            if hand[i] in counts:
                counts[hand[i]]+=1
            else:
                counts[hand[i]]=1

        while len(counts)>0:
            
            minimum=min(counts)
            for i in range(minimum,minimum+W):

                if i not in counts:
                    return False
                
                if counts[i]==1:
                    del counts[i]
                else:
                    counts[i]-=1

        return True

'''Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]'''

'''Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4'''