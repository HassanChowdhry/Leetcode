// https://leetcode.com/problems/boats-to-save-people

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people)-1
        boats = 1
        counter = 0

        total = 0
        while l <= r:
            total += people[r]
            counter += 1
            if total > limit:
                boats+=1
                counter = 1
                if total-people[r] < people[r]:
                    total = total-people[r]
                    r-=1
                    continue
                else:
                    total = people[r]
            elif counter > 2:
                boats+=1
                counter = 1
                total = 0
            r-=1
            
            if l > r:
                break
            
            total += people[l]
            counter += 1
            if total > limit:
                boats+=1
                counter = 1
                if total-people[l] < people[l]:
                    total = total-people[l]
                else:
                    total = people[l]
            elif counter > 2:
                boats+=1
                counter = 1
                total = 0
            l+=1
    
        return boats