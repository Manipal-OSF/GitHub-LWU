print("Hi")
print("hello my name is Simar")


name1 = input('Hi,Who are you ? ')
print('Welcome',name1)

age = input("What is your age ?")
print(type(age))
age = int(age)
print(type(age))    

#try and except code

name = "hello Bob"
try:
    name = int(name)
except:
    name = -1

print("Hello",name)

name2 = '123'
try:
    name2 = int(name2)
except:
    name2 = -1

print("Hello",name2)