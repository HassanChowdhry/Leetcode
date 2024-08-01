// https://leetcode.com/problems/design-hashset

class ListNode:
    def __init__(self, val=-1, next=None):
        # self.key = key
        self.val = val
        self.next = next
class MyHashSet:

    def __init__(self):
        self.set = [ListNode() for _ in range(10000)]
    
    def hash(self, key) -> int:
        return key % len(self.set)

    def add(self, key: int) -> None:
        idx = self.hash(key)
        node = self.set[idx]

        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        node = self.set[idx]

        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next
        

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        node = self.set[idx].next

        while node:
            if node.val == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)