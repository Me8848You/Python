#While loop and break and continue
# class Robot:
#     def Introduce(self):
#         print("my name is "+self.name)
#         print("my roll is "+self.roll)

# # R=Robot()
# # R.name="tom"
# # R.Introduce()

# r2=Robot()
# r2.name="makai khane ho "
# r2.roll="23"

# r2.Introduce()

# class Email:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age

#         def fun(self):
#             print("my name is "+self.Name)

# E=Email("suman","23")
# E.fun()        
# class Node:
#     def __init__(self,datavalue=None):
#         self.data=datavalue
#         self.next=None
    
# class Singleli:
#     def firstNode(self):
#         self.start=None

#     def secondNode(self):
#         newnode=Node()
#         self.next=newnode
#         print(self.newnode)

# a=Node("sunday")
# b=Node("monday")
# c=Node("tuesday")

# SSL=Singleli(a)
# SSL.secondNode(b)
# a.next=b
# b.next=c

# print(Singleli)

class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()