class Node:
    def __init__(self,data,ref=None) -> None:
        self.data=data
        self.ref=ref

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def traversing(self):
        n=self.head
        if n is None:
            print("LINKED LIST IS EMPTY")
        else:
            while n is not None:
                print(n.data)
                n=n.ref
    
    def add_begin(self,val):
        newNode=Node(val,self.head)
        self.head=newNode
    
    def del_value(self,val):
        if self.head is None:
            print("LINKED LIST IS EMPTY ALREADY")
        elif self.head.data==val:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref.data!=val:
                n=n.ref
            n.ref=n.ref.ref
            
            
            

l=LinkedList()
l.add_begin(2)
l.add_begin(5)
l.add_begin(3)
l.add_begin(1)
# l.traversing()
l.del_value(2)
l.traversing()