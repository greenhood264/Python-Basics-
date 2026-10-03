"""variables"""

name = "Vivek"
age = 23

# SheryiansSchool = "students" # pascal case
# sheryiansSchool = "students" # camel case
# sheryians_school = "students" # snake case


"""data types"""

# a = -34
# b = 56.8
# c = 12/3
# v = 34j

# print(type(v))

# st = "hello python"
# print(type(st))

# b = True
# print(type(b))


"""strings"""

# a = "VIVEK CODER"
# print(a[::])

# name = "Vivek"
# age = "23"
# print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age "))
# print(age)


# operators

# a = 5
# b = 32

# print(a + b)
# print(b - a)
# print(a * b)
# print(b//a)
# print(b/a)
# print(5**2)
# print(32%5)


# assignment operators

# a = 20

# a += 20
# a -= 10
# a *= 2
# a //= 5

# print(a)


# comparison operators

# a = 12.1
# b = 12

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


# logical operators

# print(12 > 20 and 123 > 100)
# print(12 != 12 or 23 == 45)
# print(not 12 == 12)


# if else

# a = 6

# if a > 10:
#     print("I will do task A")
# else:
#     print("I will do task B")


# num1 = int(input("please tell your first number "))
# num2 = int(input("please tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both the numbers are same")


# num = int(input("please tell your number "))

# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")


# name = input("please tell your name ")
# age = int(input("now tell your age "))

# if age >= 18:
#     print(f"hello {name} you are eligible to vote")
# else:
#     print(f"hello {name} you are not eligible to vote")


# leap year

# year = int(input("tell your year "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Its a leap year")
# else:
#     print("Its a normal year")


# for loop

# n = int(input("Which table you want ? "))

# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")


# n = int(input("please tell your number "))

# for i in range(1, n + 1):
#     print(i)


# n = int(input("please tell your number "))

# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i

# print(f"your sum is {sum}")


# factorial

# n = int(input("please tell your number "))

# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i

# print(f"your factorial is {fact}")


# even and odd sum

# n = int(input("tell your number "))

# even = 0
# odd = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i

# print(f"your even and odd sum are {even}, {odd}")


# factors

# n = int(input("which number factors you want "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


# perfect number

# n = int(input("check your number is perfect or not "))

# sum = 0

# for i in range(1, n):
#     if n % i == 0:
#         sum += i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")


# prime number

# n = int(input("check your number is prime or not "))

# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


# string reverse

# a = "VIVEK"
# b = ""

# for i in range(len(a) - 1, -1, -1):
#     b = b + a[i]

# print(b)


# palindrome

# a = "VIVEK"
# b = ""

# for i in range(len(a) - 1, -1, -1):
#     b = b + a[i]

# if b == a:
#     print("your string is palindrome")
# else:
#     print("its not a palindrome")


# count characters

# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spchr += 1

# print(f"your digits are {dig}")
# print(f"your alphabets are {char}")
# print(f"your special characters are {spchr}")


# while loop

# a = 1

# while a <= 30:
#     print(a)
#     a += 1


# reverse number

# a = int(input("tell your number "))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)


# palindrome number

# a = int(input("tell your number "))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if copy == rev:
#     print("palindromic number")
# else:
#     print("not a palindromic number")


# random guessing game

# import random

# num = random.randint(1, 10)
# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 10 "))

#     tries += 1

#     if num == guess:
#         print(f"you are right in {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")

#     else:
#         print("go a little higher")


# functions

# def hello():
#     print("this is a hello function")

# hello()


# def hello(name, age):
#     print(f"your name is {name} and your age is {age}")

# hello(age=23, name="Vivek")


# palindrome function

# def palindrome(st):
#     rev = ""

#     for i in range(len(st) - 1, -1, -1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f"{st} is a palindrome")
#     else:
#         print(f"{st} is not a palindrome")


# palindrome("VIVEK")
# palindrome("CURSOR")


# return

# def hello():
#     return "hello how are you"

# print(hello())

#Exception Handling

# a = int(input("tell your number :- "))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an err as {err}")

# else:
#     print("good there is no exception")

# finally:
#     print("i will run no matter what")


# print("ok i have done the division")

# age = int(input("tell your age :- "))

# try:

#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an error occured as {err}")


# print("the club will start soon")