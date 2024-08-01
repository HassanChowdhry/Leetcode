// https://leetcode.com/problems/design-circular-queue

class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class LL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def length(self) -> int:
        return self.len
    
    def isEmpty(self) -> int:
        return self.len == 0

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
    
    def getTail(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val
    def getHead(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

class MyCircularQueue:

    def __init__(self, k: int):
        self.list = LL()
        self.max_len = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.list.addAtTail(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.list.deleteAtIndex(0)
        return True
        

    def Front(self) -> int:
        return self.list.getHead()
        

    def Rear(self) -> int:
        return self.list.getTail()
        

    def isEmpty(self) -> bool:
        return self.list.isEmpty()
        
    def isFull(self) -> bool:
        return self.max_len == self.list.length()
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()