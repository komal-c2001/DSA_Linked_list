class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
            self.head = None
    def append(self, new_node):
        if(self.head == None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node  #appending new node
    def reverse(self):
        curr =self.head
        prev = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr 
            curr = nextnode
        self.head = prev   
    def display(self):
            temp = self.head
            print("All nodes in the list")
            while temp:
                print(temp.data)
                temp = temp.next
list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.display()
list.reverse()
list.display()

    
        
