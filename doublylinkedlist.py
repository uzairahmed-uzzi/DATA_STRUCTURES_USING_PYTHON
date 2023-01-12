class Node:
    def __init__(self,data,pref=None,nref=None) -> None:
        self.pref=pref
        self.data = data
        self.nref=nref

class LinkedList:
    def __init__(self):
        self.head=None

    def ftraversing(self):
       n=self.head
       if n is None:
           print("LINKED LIST IS EMPTY")
       else:
           while n is not None:
               print(n.data)
               n=n.nref        
    
    def btraversing(self):
       n=self.head
       if n is None:
           print("LINKED LIST IS EMPTY")
       else:
        while n.nref is not None:
            n=n.nref
        while n is not None:
            print(n.data)
            n=n.pref
    def add_begin(self,value):
        newNode=Node(value,None,self.head)
        if self.head is None:
            self.head=newNode
        else:   
            self.head.pref=newNode
            self.head=newNode
    
    def add_value(self,value,pos):
        n=self.head
        if n is None:
            print("LINKED LIST IS EMPTY SO THE GIVEN POSITION DOESN'T EXIST AND IT WILL BE INSERTED AT BEGIN")
            newNode=Node(value,None,self.head)
            self.head=newNode
        else:
            while n.data!=pos:
                n=n.nref
            newNode=Node(value,n.pref,n)
            n.pref=newNode
            n.pref.pref.nref=newNode
    
    def del_begin(self):
        n=self.head
        if n is None:
            print("LINKEDLIST IS ALREADY EMPTY")
            return
        else:
            if n.nref is None:
                self.head=None
                return
            else:
                self.head=n.nref
                n.nref.pref=None
    def del_end(self):
        n=self.head
        if n is None:
            print("LINKEDLIST IS ALREADY EMPTY")
        else:
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
            
    def del_value(self,value):
        n=self.head
        if n is None:
            print("LINKEDLIST IS ALREADY EMPTY")
            return
        else:
            if n.nref is None:
                self.head=None
                return
            else:
                while n.data!=value:
                    n=n.nref
                if n.pref is None:
                    self.head=n.nref
                elif n.nref is None:
                    n.pref.nref=None
                else:
                    n.pref.nref=n.nref
                    n.nref.pref=n.pref
                
        
l=LinkedList()
l.add_begin(1)
l.add_begin(2)
l.add_begin(3)
l.add_begin(5)
# print("BACKWARD TRAVERSING")
# l.btraversing()
l.add_value(8,1)
# print("FORWARD TRAVERSING\n")
# l.ftraversing()
l.del_value(3)
# l.del_end()
print("FORWARD TRAVERSING\n")
l.ftraversing()
    