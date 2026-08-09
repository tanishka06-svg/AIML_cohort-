''' Name:Tanishka Sanjay Shirode 
    Batch: AIML
    Day:1(9-8-26)
    Assignment No: 1
    It Includes:
'''
# Why we use python for AIML?
''' Python is widely used in AI and Machine Learning (AIML) because it is simple, easy to learn
    And python has powerful libraries.
    These libraries make it easier to build machine learning models, and develop AI applications quickly.'''
# Datatypes in Python
a=2
b=2.5
c="Good Morning"
print(type(a))
print(type(b))
print(type(c))

# Taking inputs in Python  
y=int(input("Enter a Number:"))
print(y)

# Data Structures in Python
dict={'a':"Rahul",'y':"Rohan", 'z':"Raj"} #Dictionary
print(dict)
print(type(dict))
print(dict["y"])


list=[1,'abc','this','is','list','True',90.54,dict] #List
print(list)
print(type(list))
print(list[6])

t1=[6,8,4,9,12] #Tuple
t2=[1.2, 4.6, 9.2]

print(type(t1))
print(t1)

# Tuple operations

#Acessing Elements
print(t1[1])

# Slicing operation
print(t1[3:6])

# Tuple Concatination
print(t1+t2)

#Repetition
print(t1*2)

#Membership
print(6 in t1)

#Length
print(len(t1))

#Count
print(t1.count(12))

#Index
print(t1.index(8))

# Slicing of Strings
s="Today's day is a Sunday."

print(s[:6])
print(s[2:])
print(s[11:14])

#Conditional Statements in Python

a=int(input("Enter your Age:"))
if a<18:
    print("You are a Teenager")
else:
    print("You are an Adult")

#Loops in Python

# While Loop
i = 1

while i <= 5:
    print(i)
    i = i + 1

# for loop
for i in range(1, 6):
    print(i)
