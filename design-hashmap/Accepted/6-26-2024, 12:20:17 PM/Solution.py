// https://leetcode.com/problems/design-hashmap

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        # cur = self.map[self.hashcode(key)]
        idx = key % len(self.map)
        node = self.map[idx]

        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = ListNode(key, value)
         
    def get(self, key: int) -> int:
        # cur = self.map[self.hashcode(key)].next
        idx = key % len(self.map)
        node = self.map[idx].next
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        # cur = self.map[self.hashcode(key)]
        idx = key % len(self.map)

        node = self.map[idx]
        while node.next and node.next.key != key:
            node = node.next
        if node and node.next:
            node.next = node.next.next
