// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        mp = {skills[i]: i for i in range(len(skills))}
        count = 0
        mx = max(skills)
        if k > len(skills):
            return mp[mx]
        prev = -1
        while count < k:
            p1, p2 = skills[0], skills[1]
            # print(skills, count, prev)
            if p1==mx or p2==mx:
                return mp[mx]

            if p1 > p2:
                skills.append(skills.pop(1))
                if prev == p1:
                    count+=1
                else:
                    count=1
                    prev = p1
            else:
                skills.append(skills.pop(0))
                if prev == p2:
                    count+=1
                else:
                    count=1
                    prev = p2
            
        
        return mp[skills[0]]
