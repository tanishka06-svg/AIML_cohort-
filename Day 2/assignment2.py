# Combined Code from all notebook cells

''' Name:Tanishka Sanjay Shirode
    Batch: AIML
    Day:2(10-8-26)
    Assignment No: 2
    It Includes:
'''

#Arithmetic operaters in Python

#Exponent
a=2**3
print(a)

#Modulus
b=15%2
print(b)

#Integer Division
c=25//5
print(c)

#Division
d=25/5
print(d)

#Multiplication
e=3*4
print(e)

#Addition
f=10+9
print(f)

#Subtraction
g=20-10
print(g)


#String Concatination
a="Hello"
b="World"
c=""
d=a+b+c
print(d)


#String Replication

x="Hii"
y=5
z= x*y
print(z)


#Changing value of variable

s1=7.5
print(s1)
s1="Hello"
print(s1)


#Typecasting in Python

a=18.67
b=str(a)
print(type(b))


c="12"
d=int(c)
print(type(d))


e="13.6"
f=float(e)
print(type(f))


#Gives the round up value of the number
x=19.5000
y=round(x)
print(y)


#absolute function gives the mod vlaue of the number
x=-80.7000
y=abs(x)
print(y)


#Comparison operators in Python

a=float(input("Enter first Number"))
b=float(input("Enter Second"))

if a==b:
  print("They are Equal")

elif a!=b:
  print("They are not equal")

elif a>b:
  print("a is greater")

elif a<b:
  print("a is lesser")

elif a>=b:
  print("a is greater or equal to b")

else:
  print("Bye")

#Logical operators in python
#Logical operators in python

a= 20
b= True

#AND operator
print(a>=18 and b)

#OR operator
print(a>=18 or b)

#NOT operator
print(not b)


# Python game using Arithmetic Operators

print("SYSTEM: You are locked inside the Python Vault.")
print("Your Mission: Collect enough power to escape the vault.")

#level 1
energy=10
print("LEVEL 1 — ENERGY CORE")
print(f"You start with {energy} energy.")

found = int(input("You found an energy crystal worth: "))

energy = energy + found

print("Energy collected!")
print(f"Your energy is now: {energy}")

#level 2
print("LEVEL 2 — POWER BOOST")

boost = int(input("Choose your power multiplier (1–5): "))

powered_energy = energy * boost

print("POWER ACTIVATED!")
print(f"Your energy became: {powered_energy}")

#level 3
print("LEVEL 3 — LASER WALL")

laser_cost = int(input("How much energy does the laser wall cost? "))

remaining = powered_energy - laser_cost

print("Laser wall disabled!")
print(f"Energy remaining: {remaining}")

#level 4
print("LEVEL 4 — TEAM UP")

team_size = int(input("How many hackers are in your team? "))

share = remaining / team_size

print(f"Each hacker gets {share:.2f} energy.")

#level 5
print("LEVEL 5 — BUILD THE SQUAD")

energy_per_hacker = int(input("Energy required per hacker: "))

full_hackers = remaining // energy_per_hacker

print(f"You can fully power {full_hackers} hackers.")

#level 6
leftover = remaining % energy_per_hacker

print(f"Energy left unused: {leftover}")

#level 7
print("LEVEL 7 — THE FINAL VAULT")

power_level = int(input("Enter your final power level: "))

final_power = power_level ** 2

print(f"Your final power is: {final_power}")

#escape
print("VAULT UNLOCKED!")

print(f"""
🏆 MISSION COMPLETE!

🔋 Final energy      : {remaining}
👥 Full hackers      : {full_hackers}
♻️ Leftover energy   : {leftover}
⚡ Final power       : {final_power}

You didn't just learn operators.
You used them to build something. 🐍

WELCOME TO PYTHON.
""")