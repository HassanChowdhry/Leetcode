// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        curr, end = self.head, self.tail
        if not curr or index >= self.len:
            return -1

        for i in range(index):
            curr = curr.next
        
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.len += 1
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
            return
            
        new_node = Node(val, self.head)
        self.head.prev = new_node
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        self.len += 1
        if not self.tail:
            self.head = Node(val)
            self.tail = self.head
            return

        new_node = Node(val, None, self.tail)
        self.tail.next = new_node
        self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.len:
            self.addAtTail(val)
            return
        
        
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        
        nxt = curr.next
        new_node = Node(val, nxt, curr)
        curr.next = new_node
        nxt.prev = new_node
        self.len += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.len -= 1
            return
        if index == self.len-1:
            self.tail = self.tail.prev
            if not self.tail:
                self.head = None
            self.len -= 1
            return

        curr = self.head
        for i in range(index-1):
            curr = curr.next
        
        nxt = curr.next.next
        curr.next = nxt
        nxt.prev = curr
        self.len -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)