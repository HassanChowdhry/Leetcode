// https://leetcode.com/problems/hand-of-straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        split = len(hand)//groupSize
        if groupSize == 1:
            return True
        if len(hand)/groupSize != split:
            return False
        
        # set up - Sort values, visit set 
        hand.sort()
        visit = set()
        res = []
        
        # logic - iterate untill you can populate subgroup keep count
        for i in range(split):
            sub = []
            for pos, card in enumerate(hand):
                if len(sub)==groupSize:
                    break
                if pos in visit:
                    continue
                if sub and sub[-1]==card:
                    continue
                
                visit.add(pos)
                if not sub:
                    sub.append(card)
                    continue

                if sub[-1]+1 != card:
                    return False
                sub.append(card)

            if len(sub) != groupSize:
                return False

        return True