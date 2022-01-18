# x = 35
# y = 5
# print(x)
# print(y)
# o="string"
# print(o)
# x=int(2.44)
# print(x)
# print(type(x))

# y=str(345)
# print(y)
# print(type(y))

# # next variable topic
# #overwritten variable
# a=123
# a="suman"
# print(a)

# a,b,c="orange",'black','blue'
# print(a)
# print(b)
# print(c)

#unpacked list
# fruits=['apple ', 'banana' , 'cactus']
# x,y,z,=fruits

# print(x)
# print(y)
# print(z)

#+used of + for adding the character
# x='awesome'
# print("python is "+x)
# x="python is "
# y="just wow"
# print(x+y)

# a=5
# b=35
# print(a+b)
# b=34
# c=a+b 
# print(c)
# x="wow"
# def addition():
#     print("the PYTHON is "+x)

# addition()
#or simply you can use global keyword 

#let's see one more example
# def add():
#     global x
#     x="23"
#     print("the sum is "+ x)

# add()
# print("my roll is also "+x)
# p=-878.88
# print(type(p))
# p=34e13
# print(type(p))
# p=34E13
# print(type(p))
# t=3+5j
# print(type(t))

#type conversion 
# x=1
# y=9.0
# z="34"
# a=chr(x)
# print(type(a))
# b=float(z)
# print(type(b))
# print(b)

#INPORT SECTION
# import random
# print(random.randrange(1,10))

# txt=" hello world! "
# x = txt.strip()
# print(x)

# fruits = {"banana" , "apple", "hello world"}
# more_fruits = ["aanar","thulo anarr"]
# fruits.update(more_fruits)
# print(fruits)
# if "hello world" in fruits:
#     print("hello world is present in the list")

# #if loop
# a = 25
# b = 35
# if a > b:
#      print("a is greater ")
# else:
#      print(" b is greater")

    #  while loop wala
i = 1
# while i < 5:
#         print(i)
#         i=+1
# i = 1
# while i < 6:
#   print(i)
#   i += 1
a = 1
# while a < 10:
#     print(a)
#     if a == 5:
#         break
#     a += 1
# while a < 10:
#     print(a)
#     if a == 5:
#         continue
#     a += 1
    
# i = 1
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
# #   i += 1
# i = 1
# while i < 10:
#     print(i)
#     i += 1
#     if i == 7:
#        break
# # i = 1
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
    
             
# a = 2
# while a < 10:
# #     print(a)
# #     a += 1
# #     if a == 5:
# #         break
# # Dictionary datatypes 
# thisdict {
#     "nepal":"kathmandu",
#     "india":"delhi",
#     "ford": "JCB",
#     "start": 1234
# }
# print(thisdict(ford))
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# a=["apple","ball","cat",1,3,True]
# print(a)
# a[0]="banana"
# print(type(a))
# print(a)


# print(aaa)
# a=aaa.keys()
aaa={
     "brand":"FORD",
     "model":"Mustang",
     "year": 134213
}
aaa["model"]="picaso"
aaa["color"]="red"
# b=list((aaa))
# print(aaa)
# b=aaa.values()
b=tuple((aaa))
print(b)
        