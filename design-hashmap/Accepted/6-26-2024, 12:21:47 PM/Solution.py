// https://leetcode.com/problems/design-hashmap

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        idx = key % len(self.map)

        node = self.map[idx]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        new_node = ListNode(key, value)
        node.next = new_node

    def get(self, key: int) -> int:
        idx = key % len(self.map)
        node = self.map[idx].next

        while node:
            if node.key == key:
                return node.val
            node = node.next
        
        return -1

    def remove(self, key: int) -> None:
        idx = key % len(self.map)

        node = self.map[idx]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)