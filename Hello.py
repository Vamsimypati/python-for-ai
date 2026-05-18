#strings
string = "My Name Is Vamsi"
my_Long_string = """
My Name Is Vamsi.
I AM From Andhra Pradesh,Nellore
"""
first_name = "Vamsi"
last_name = "Mypati"

Full_name = first_name + " " + last_name
long_dash = "-" * 25
print(Full_name)
print(long_dash)
len(Full_name)

is_True = True
age = 19
can_vote = age >= 18
age = 25
has_License = False

#AND - Both Must Be True
can_drive = age >= 16 and has_License
print(can_drive)


age = 25
has_License = True
drunk = True

can_drive = age >= 16 and has_License and not drunk

#strings
name = "Vamsi"
string = f"Hi, I AM From India {name}"

#string Methods
name = "Vamsi"

name.lower()
name.upper()

Sentence = "Hi My Name Is Vamsi"
Sentence.title()

#control flow
#-> if Statements
temperature = 32
if temperature > 30:
    print("It Very Hot")
if temperature > 25:
    print("IT Tooo Hot")
else:
    print("It is Nice Weather")

#if-elif Statements
score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good Job!")
elif score >= 70:
    print("C - Keep It Well")
else:
    print("D - Need Improvement")

# Multiple Conditions
age = 25
has_license = True
if age >=18 and has_license:
    print("You Can Drive")
else:
    print("You Cannot Drive")

# Nested If Statements
has_Ticket = True
age = 18

if has_Ticket:
    if age >= 18:
        print("Enjoy The Movie!")
    else:
        print("Need Supervision!")
else:
    print("You Need To Buy A Ticket")

# Loops
for i in range(7):
    print("Hello World!")
# Loops Start count from diffent Starting Points
for i in range(1, 6):
    print(i)

#count by 2s
for i in range(0, 10, 2):
    print(i)

#Lists
age = 20
has_License = True
My_list = ["Vamsi", 25, age, False, has_License]

#Accessing items
print(My_list[1])

#change List
My_list[0] = "Sai" 

# Add The List
My_list.append("Mypati")

# Insert The List
My_list.insert(1, "Vamsi")

# Remove The List
My_list.remove(25)

#Dictionary
person = {
    "Name" : "Vamsi",
    "age" : 20,
    "Country" : "India"
}
person["Name"] = "Mypati"

person["License"] = "True"
del person["License"]

# Tuple
empty = ()
point = (3, 5)
colors = ("red", "Green", "Blue")
print(colors[0])

# sets
empty_sets = set()

number = {1, 2, 3, 4, 5}
fruits = set(["Apple", "Bannana", "Grapes"])

# in Sets Remove Duplicate
score = {67, 89, 98, 67, 89, 90}
unique_score = set(score)