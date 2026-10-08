class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkList:
    def __init__(self, head=None):
        self.head = head

    def insertAtPos(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1
            # Walk until temp is sitting at position pos - 1
            while p < pos - 1 and temp is not None:
                temp = temp.next
                p += 1
            
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node

    def insertATEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


# Test Run
obj = SinglyLinkList()
obj.insertATEnd(10)   # [10]
obj.insertATEnd(20)   # [10, 20]
obj.insertATEnd(30)   # [10, 20, 30]

obj.insertAtPos(Node(100), 1)  # Insert 100 at pos 1 -> [100, 10, 20, 30]
obj.insertAtPos(Node(66), 4)   # Insert 66 at pos 4  -> [100, 10, 20, 66, 30]

obj.printLL()