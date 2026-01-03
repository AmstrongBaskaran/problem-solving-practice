# age = int(input("Enter age"))
# if age < 18 and age > 0:
#     print("150")
# elif age >= 18 and age <= 60:
#     print("250")
# elif age > 60:
#     print("100")
# else:
#     print("invalid input")


# A stadium sells entry passes with the following rules:
# * If age < 12 → Ticket = ₹50
# * If age between 12–59 → Ticket = ₹120
# * If age ≥ 60 → Ticket = ₹80
# Additionally, if the person’s age is a Even number, give a ₹5 discount.
# Get the input from the user and return the final discounted stadium ticket price.

# Sample Input:
# 59

# Sample Output:
# 120
# tk = 0
# age = int(input("Enter age"))
# if age < 12:
#     tk = 50
# elif age >= 12 and age <=59:
#     tk = 120
# elif age >= 60:
#     tk = 80
# if age % 2 == 0:
#     print(tk-5)
# else:
#     print(tk)


# Question 3:
# A shopkeeper has n mangoes.
# He wants to pack them into baskets, with 5 mangoes in each basket.

# Write a program to calculate:
# * How many full baskets can be made
# * How many mangoes will be left

# Sample Input:
# 23

# Sample Output:
# Full Basket is 4
# Left Over mangoes is 3
# n = int(input("Enter Mangoes"))
# FullBasket = n // 5
# print("FullBasket = ",FullBasket)
# Leftover = n % 5
# print("Leftover = ",Leftover)

# Question 4:
# A child has n candies and eats one candy each day until all are finished.
# Write Python program to print how many candies the child ate and how many are left each day.
# Sample Input:
# 3
# Sample Output:
# Day 1 = 2 left
# Day 2 = 1 left
# Day 3 = 0 left

# n = int(input("enter candies"))
# for i  in  range (1,n+1):
#     candies_left = n - i
#     print("Day",i,"=",candies_left,"left")


# Question 5:

# An employee gets a monthly salary.

# * If sales ≥ 100 units → bonus = 10%
# * 50–99 units → bonus = 5%
# * <50 → no bonus

# Write a program that asks for salary and sales and prints total salary including bonus.

# Sample Input:
# Enter your salary 40000
# Enter your sales 120

# Sample Output:
# Bonus = 4000
# Total Salary = 44000

# Write a function to print all numbers from a to b using a loop.
# def print_numbers(a, b):
#     # write your code here
# print_numbers(1, 5)
# print_numbers(3, 8)
# print_numbers(10, 12)

# a = int(input("num1"))
# b = int(input("num2"))

# for i in range(a,b+1):
#     print(i)


# Write a function to print all numbers from b to a in reverse order using a loop.
# def print_reverse(b, a):
#     # write your code here
# print_reverse(10, 5)
# print_reverse(7, 1)
# print_reverse(20, 15)

# a = int(input("num1"))
# b = int(input("num2"))
# for i in range(b,a-1,-1):
#     print(i)

# Write a function to print all even numbers between a and b using a loop.
# def print_even(a, b):
#     # write your code here
# print_even(1, 10)
# print_even(4, 12)
# print_even(7, 15)

# a = int(input("num1"))
# b = int(input("num2"))
# for i in range(a,b+1):
#     if i % 2 == 0:
#         print(i)

# Write a function to print all numbers between a and b that are divisible by a given number n.
# def print_divisible(a, b, n):
#     # write your code here
# print_divisible(1, 20, 3)
# print_divisible(10, 30, 5)
# print_divisible(5, 25, 7)

# n = int(input("enter divisible number"))
# a = int(input("num1"))
# b = int(input("num2"))
# if n == 0:
#      print(" 0 not div num")
# else:
#      for i in range(a,b+1):
#           if i%n == 0:
#               print(i)


# Write a function to print all odd numbers between a and b in reverse order using a loop.
# def print_odd_reverse(a, b):
#     # write your code here
# print_odd_reverse(1, 10)
# print_odd_reverse(5, 15)
# print_odd_reverse(10, 20)

# a = int(input("num1"))
# b = int(input("num2"))
# for i in range(b,a-1,-1):
#     if i % 2 != 0:
#          print(i)

# Write a function to count how many odd numbers are between a and b.
# def count_odd(a, b):
#     # write your code here
# count_odd(1, 10)
# count_odd(5, 20)
# count_odd(10, 15)

# a = int(input("num1"))
# b = int(input("num2"))
# count = 0
# for i in range(a,b+1):
#     if i % 2 != 0:
#         count+=1
# print(count)


# Write a function to count how many numbers are divisible by a given number between a and b.
# def count_divisible(a, b, n):
#     # write your code here
# count_divisible(1, 10, 2)
# count_divisible(5, 25, 3)
# count_divisible(10, 50, 5)

# n = int(input("enter divisible number"))
# a = int(input("num1"))
# b = int(input("num2"))
# count = 0
# for i in range(a,b+1):
#         if i % n == 0:
#             count+=1
# print(count)

# word = "Python"
# rev = ""
# for i in range(len(word)):
#     rev = rev + word[i]
# print(rev[::-1])

# text = "education"
# count = 0
# for i in text:
#     if i in ['a','e','i','o','u']:
#         count += 1
# print(count)

# nums = [9, 5, 2,3, 8]
# min_num = nums[0]
# for i in range(len(nums)):
#     if nums[i] < min_num:
#         min_num = nums[i]
# print(min_num)

# arr = ["ram","raj","ravi","ramesh","ramki"]
# salary = [120,234,567,789,789]
# max_salary = salary[0]
# for i in range(len(salary)):
#     if salary[i] > max_salary:
#         ma = salary[i]
# for i in  range(len(salary)):
#     if salary[i] == ma:
#         print(arr[i])



# Find Common Hobbies
# Story:
#  Two friends, Arjun and Priya, wrote down their favorite hobbies. They want to know which hobbies they share in common.
# Task:
#  Given two lists, find the common hobbies.
# Example Input:

# arjun = ["reading", "swimming", "painting", "music"]
# priya = ["music", "dancing", "reading"]


# arjun = ["reading", "swimming", "painting", "music"]
# priya = ["music", "dancing", "reading"]
# temp = []
# for i in priya:
#     if i in arjun:
#         temp.append(i)
# print(temp)      


# 2. You are given two lists:
#  fruits = ["apple", "banana", "mango"]
#  colors = ["red", "yellow", "green"]
#  Ask the user for a color, and print which fruit has that color.
# Input: "yellow"
# Output: banana
# fruits = ["apple", "banana", "mango"]
# colors = ["red", "yellow", "green"]
# color = input("enter color")
# for i in range(len(colors)):
#     if colors[i] == color:
#         print(fruits[i])

# Take a string and a character as input, and print all the positions (indexes) where that character occurs.
# Input:
# word = "banana"
# char = "a"
# Output: 1, 3, 5

# word = "banana"
# char = "a"
# res = []
# for i in range(len(word)):
#     if word[i] == char:
#         res.append(i)
# print(res)
# 4. Reverse Each Word in a Sentence
# Reverse each word separately but keep their order.
# Input: "I like Python"
# Output: "I ekil nohtyP" (edited)

# word = "amstrong"
# letter = list(word)
# print(letter[::-1])


# word = "I like python"
# word_lst=[]
# temp=''
# for i in word:
#     if i==" ":
#         word_lst.append(temp)
#         temp=""
#     else:
#         temp+=i
# word_lst.append(temp)

# for i in range(len(word_lst)-1,-1,-1):
#     print(word_lst[i], end=' ')

# word = "banana"
# char = input("enter a char")
# res = []
# if char in word:
#     for i in range(len(word)):
#         if word[i] == char:
#             res.append(i) 
#     print(res)
# else:
#     print("invalid char")


# word = "i like python"
# wld = []
# temp = ""
# for i in range(len(word)):
#     if word[i] == " ":
#         wld.append(temp)
#         temp = ""
#     else:
#         temp += word[i]
# wld.append(temp)
# for i in range(len(wld)-1,-1,-1):
#     print(wld[i],end=" ")

# last_month_score = [45, 60, 70, 55, 80]
# this_month_score = [50, 58, 75, 65, 78]
# for i in range(len(last_month_score)):
#     if last_month_score[i] > this_month_score:
#         print(this_month_score[i])


# l_m = [45,60,54,23,30]
# t_m = [50,61,54,23,30]
# for i in range(len(l_m)):
#     if t_m[i] > l_m[i]:
#         print(i+1,end=" ")
# count = 0
# count1 = 0
# add = 0
# sums = 0
# ans1 =0
# ans2 = 0
# for i in range (len(gen_list)):
#     if gen_list[i] == "M":
#         add += marks_list[i]
#         count += 1
#         print(ans1)
#     elif gen_list[i] == "F":
#         sums += marks_list[i]
#         count1 = 0
#         print(ans2)
#         ans2 = sums/count1
#         ans1 = add/count

# arr = "((()))()"
# open_count = 0
# close_count = 0
# for i in range(len(arr)):
#     if arr[i] == "(":
#         open_count += 1
#     elif arr[i] == ")":
#         close_count += 1
# ans = open_count-close_count
# if ans == 0:
#     print("true")
# else:
#     print("false")

# count = 0
# word = input("enter sentence")
# pangram = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in pangram:
#     if i in word:
#         count += 1
# if count == 26:
#     print("true")
# else:
#     print("false")

# arr = "too hot to hoot"
# rev = ""
# stright = ""
# space = " "
# for i in range(len(arr)-1,-1,-1):
#     if arr[i] != space:
#         rev += arr[i]
# for j in range(len(arr)):
#     if arr[j] != space:
#         stright += arr[j]
# if stright == rev:
#     print(True)
# else:
#     print(False)

# arr = "aeiou 32"
# number = '0123456789'
# vowel = "aeiouAEIOU"
# count = 0
# sum = 0
# for i in arr:
#     if i in vowel:
#         count += 1
# for j in arr:
#     if j in number:
#         sum += int(j)
# if count == sum:
#     print(True)
# else:
#     print(False)

arr = "The quick brown fox jumps over the lazy dogg"
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0
for i in alphabet:
    if i in arr:
        count += 1
if count == 26:
    print(True)
else:
    print(False)

    