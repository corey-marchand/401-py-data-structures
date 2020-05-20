class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList(object):
    def __init__(self):
        self.newNode = None
    
    def insert(self, data):
        new_Node = Node(data)
        if(self.newNode):
            current = self.newNode
            while(current.ref):
                current = current.ref
            current.ref = new_Node
        else:
            self.newNode = new_Node

    def includes(self,x):
        current = self.newNode

        while current != None:
            if current.data == x:
                return True
            current = current.ref
        return False
    
    def _str_(self):
        current = self.newNode
        while(current):
            print(current.data)
            current = current.ref
    
    def kthFromTheEnd(self, k):
        counter = 0
        current = self.newNode
        while current:
            counter = counter + 1
            current = current.ref
        kstart = counter -1 -k
        if kstart < 0 and k < 0:
            kstart = kstart -1
            current = current.ref
        print(current) 

if __name__=='__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(14)
    ll.insert(15)
    ll.insert(13)
    ll.insert(4)
    # ll._str_()
    ll.kthFromTheEnd(0)
    # if ll.includes(13):
    #     print("yes")
    # else:
    #     print("no")


