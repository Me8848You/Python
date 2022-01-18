class Node:
    def __init__ (self, value=None, next=None):
        self.v=value
        self.n=next

class SSL:
    def __init__(self):
        self.start=None
        print('SSL(OBJ) IS CREATED')
        
    def first(self,val):
        newnode=Node(val)
        self.start=newnode
    def traverse(self):
        tmp=self.start
        if tmp!=None:
            print(tmp.v)
            tmp=tmp.n



x=SSL()
x.first(6)
x.traverse()


# class Node:
#     def __init__(self,value=None,next=None):
#         self.val=value
#         self.nxt=next

# class SSL:
#     def __init__(self):
#         self.start=None
#         print("The SSL constructor is called i.e Object banyoo")
        
#     def firstnode(self,Value):
#         newnode=Node()
#         self.data=Value
#         self.pointer=None

# A=SSL()
# A.start="23"
# A.firstnode.data="5"

