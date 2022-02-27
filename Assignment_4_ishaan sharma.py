print('-----------------------------------------------------------------')
print('Question 1')
print("")
print("The problem of tower of Hanoi with three disks.")
print("")
def hanoi(n, fro_m, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro_m, aux, to)
    print(f"Move Disk {n} from {fro_m} to {to}")
    hanoi(n-1, aux, to, fro_m)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
print("")

###################################################################################

print("------------------------------------------------------------------")
print('Question 2')
print(" ")
print(" ")
#input rows
n = int(input("Enter the number of rows in Pascal's Triangle = "))

#using recursions
print("\nUsing recursions =\n")
def pascal(n, original_n=n):
    if n == 0:
        return
    
    pascal(n-1,original_n)

    #printing the spaces
    print('  '*(original_n-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\nUsing loops =\n")
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

#####################################################################################

print("-------------------------------------------------------------------")
print('Question 3')
print("")
print(" ")

print(" ")
a=int(input("Enter the first integer = "))
b=int(input("Enter the second integer = "))
c=a%b
d=a//b
print("Remainder is = ", c)
print("Quotient is = ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set = ", frozenset(set1))
print("Largest value in the set = ", max(set2))
k=max(set2)
print("Hash value = ", hash(k))
print("")

###################################################################################

print("-------------------------------------------------------------------")
print('Question 4')
print("")
print(" ")
print(" ")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Ishaan Sharma", 21103043)
print("Object created")

#printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")

#####################################################################################

print("-------------------------------------------------------------------")
print('Question 5')
print("")
print(" ")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee1 = Employee("Mohan", 40000)
employee2 = Employee("Rohan", 50000)
employee3 = Employee("Vivek", 60000)

#part a, updating salary
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b, deleting a record
print("b. ", end='')
del employee3

print(" ")

#####################################################################################

print("-------------------------------------------------------------------")
print('Question 6')
print("")
print(" ")
print(" ")
#inputting a word from the first friend
word = input("Enter the first word: ")

#inputting a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word's meaning
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print("")

 ####################################################################################
