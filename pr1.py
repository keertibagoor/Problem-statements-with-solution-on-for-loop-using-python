# print numbers from 1 to 10
for i in range(1,11):
     print(i)

#print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

#print all even numbers from 1 to 100
for i in range(2, 101, 2):
    print(i)

#print all odd numbers from 1 to 100
for i in range(1, 101, 2):
    print(i)

#find sum of numbers from 1 to N
sum = 0
N = int(input("enter a number: "))
for i in range(1, N+1):
    sum += i
print(sum)

#find the product of number fro 1 to N (fectorial)
product = 1
N = int(input("Enetr a number: "))
for i in range(1, N+1):
    product *= i
print(product)

#count how many number are between 1 to N
count = 0
N = int(input("Enetr a number: "))
for i in range(1, N+1):
    count += 1
print(count)

#print the multiplication table of a given number
num = int(input("enter a table number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

#Find the sum of all even numbers from 1 to N.
sum =0
N = int(input("Enter a number: "))
for i in range(2, N+1, 2):
    sum += i
print(sum)

#Find the sum of all odd numbers from 1 to N.
sum =0
N = int(input("Enter a number: "))
for i in range(1, N+1, 2):
    sum += i
print(sum)

#Count the number of digits in a number.
num = input("enter a number: ")
count = 0
for i in num:
    count += 1  
print(count)

#Reverse a number.
num = input("enter a number: ")
for i in num[::-1]:
    print(i, end="")

#Check whether a number is a palindrome.
num = input("Enter a number: ")
if num == num[::-1]:
    print("pelindrom")
else:
    print("not a pelindrome")

#Find the sum of digits of a number.
num = input("Enter a number: ")
sum= 0
for i in num:
    sum += int(i)
print(sum)

#Check whether a number is an Armstrong number.
num = input("enter a number: ")
#{ for i in num:
#     count +=1 } instead of this only use {len(num)}
count = len(num)
sum = 0
for i in num:
    sum += int(i)**count
if sum == int(num):
    print("armstrong number")
else:
    print("not armstrong number")
    
#Check whether a number is a Strong number.
num = input("enter a number: ")
sum = 0
for i in num:
    fact = 1
    for j in range(1, int(i)+1):
        fact *= j
    sum += fact
if sum == int(num):
    print("strong number")
else:
    print("not strong number")

#Check whether a number is a perfect number.
num = input("Enter a number: ")
sum =0
for i in range(1,int(num)):
    if int(num) % i == 0:
        print(i)
        sum += i
if sum == int(num):
    print("perfect number")
else:
    print("not perfect number")

#Print all factors of a number.
num = input("Enter a number: ")
sum =0
for i in range(1,int(num)+1):
    if int(num) % i == 0:
        print(i)

#Check whether a number is prime.
num = input("Enter a number: ")
count = 0
for i in range(1, int(num)+1):
    if int(num) % i == 0:
        count += 1
if count ==2:
    print("prime number")
else:
    print("not a prime number")
