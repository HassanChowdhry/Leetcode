// https://leetcode.com/problems/find-median-from-data-stream

import bisect 
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:

        n = len(self.arr)
        mid = (n-1) // 2
        print(mid)
        if n % 2:
            return self.arr[mid]
        else:
            left = self.arr[mid]
            right = self.arr[mid+1]
            return (left + right) /2 

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()