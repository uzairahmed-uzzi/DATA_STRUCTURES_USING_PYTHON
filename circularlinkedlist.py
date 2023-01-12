class Node:
    def __init__(self,data,ref=None) -> None:
        self.ref=ref
        self.data = data

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        
    def add_begin(self,val):
        if self.head is None:
            newNode=Node(val,self.head)
            self.head=newNode
        else:
            if self.head.ref is None:   
                newNode=Node(val,self.head)
                self.head=newNode
                n=self.head
                while n.ref is not None:
                    n=n.ref
                n.ref=self.head
            else:
                n=self.head
                while n.ref is not self.head:
                    n=n.ref
                newNode=Node(val,self.head)
                self.head=newNode                
                n.ref=self.head

    
    def traversing(self):
        n=self.head
        if n is None:
            print("LINKED LIST IS EMPTY ALREADY")
        else:
            if n.ref is None:
                print(str(n.ref)+"-->"+str(n.data))
            else:
                
                while n.ref is not self.head:
                    print(str(n.ref)+"-->"+str(n.data))
                    n=n.ref
                print(str(n.ref)+"-->"+str(n.data))




        
        

l=LinkedList()
l.add_begin(1)
l.add_begin(2)
l.add_begin(3)
l.add_begin(4)
l.add_begin(5)
# l.add_begin(4)
l.traversing()