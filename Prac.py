# Question 1:
# A cinema charges:
# * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60
# Write a program that asks for age and prints the ticket price.
# Sample Input:
# 65
# Sample Output:
# 100
# Question 2:
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
# Question 4:
# A child has n candies and eats one candy each day until all are finished.
# Write Python program to print how many candies the child ate and how many are left each day.
# Sample Input:
# 3
# Sample Output:
# Day 1 = 2 left
# Day 2 = 1 left
# Day 3 = 0 left

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

# salary = int(input("salary"))
# sales = int(input("sales"))
# if sales >= 100:
#     bonus = salary/100 * 10
#     print(bonus+salary)
# elif sales >= 50 and sales <= 99:
#     bonus = salary/100 * 5
#     print(bonus+salary)
# else:
#     print(salary)


# Question 6:
# Earnings of a Salesperson:
# * 5% commission for sales ≤ ₹5000
# * 10% for sales 5001–10000
# * 15% for sales > 10000
# Input weekly sales of the salesperson and calculate commission.
# Test Cases with their output:
# 7000 -> 700
# 12000 -> 1800
# 11000 -> 1650

# sales =int(input("sales amount"))
# if sales <= 5000:
#     comi = sales/100*5
#     print(comi)
# elif sales > 5000 and sales <= 10000:
#     comi = sales/100*10
#     print(comi)
# else:
#     comi = sales/100*15
#     print(comi)



# Question 7:
# Multi-Item Shopping Discount
# * Price > 100 → 10% discount
# * Price 50–100 → 5% discount
# * Price <50 → no discount
# Print discounted price per item
# Test cases with their output:
# 200 → 180
# 80 → 76
# 40 → 40
# 150 → 135




# Question 8:
# A file manager needs to classify files based on their extension.
# .csv  → print output as "This is an Excel File"
# .jpg  → print output as "This is a JPEG File"
# .doc  → print output as "This is a Word File"
# .pdf → print output as "This is a PDF File"
# .py → print output as "This is a Python File"
# .Any other input, print output as "Unknown File Type"
# Print the result based on the input
# Sample Input:
# .csv
# Sample Output:
# This is an Excel file
# Sample input:
# .py
# Sample Output:
# This is a Python File
# file = input("enter your file name:(.jpg,.csv,.doc,.pdf,.py,.Any,):")
# if file == '.csv':
#     print("This is an Excel File")

# Question 9:
# Taxi charges:
# * First 10 km → ₹15/km
# * Next 20 km → ₹12/km
# * Beyond 30 km → ₹10/km
# Estimate the Taxi charges based on the input and print the output.
# Sample Input:
# 15  → 180
# 35 → 350
# 10 → 150

# km = int(input("enter you km"))
# if km <= 10:
#     price = km*15
#     print(price)
# elif km <= 20:
#     price =km*12
#     print(price)
# else:
#     price = km*10
#     print(price)



# Question 10:
# Lily is N years old.
# On every odd birthday (1, 3, 5, …) → she gets 1 toy.
# On every even birthday (2, 4, 6, …) → she gets money.
# The money starts at ₹10 on her 2nd birthday.
# On each next even birthday, it increases by ₹10 more:
# 2nd birthday → ₹10
# 4th birthday → ₹20
# 6th birthday → ₹30
# and so on.
# At the end, print the following:
# * Number of toys Lily has.
# * Total money she has (money from even birthdays after brother takes ₹1).
# Input
# * Lily’s age (N)
# * Nothing else (price of toys is not needed because we are not selling)
# Output
# * Number of toys
# * Total money (formatted with 2 decimal places)
# Sample TestCase:
# Input
# 10
# Output
# 5
# 150.00
# Explanation:
# Toys → 1,3,5,7,9 → 5 toys.
# Money → 10 + 20 + 30 + 40 + 50 = ₹150. 

# n = int(input("enter age"))
# money = 0
# sum = 0
# for i in range (1,n+1):
#     if i % 2 == 0:
#          money +=10
#          sum += money
#          print(sum)


# Write a function to calculate total reward for a given number of steps.
#  For every 1000 steps → ₹5
#  Every 5000th step → bonus ₹20
# def total_reward(steps):
#     # write your code here
# total_reward(4000)
# total_reward(6000)
# total_reward(10000)

# steps = int(input("enter steps"))
# cost=0
# for i in range(1000,steps+1,1000):
#     if i%5000==0:
#         cost+=25
#     else:
#         cost+=5
# print(cost)


# Write a function to find how many un-popped balloons remain after n balloons are inflated.
#  Every 4th balloon pops automatically.

# Write a function to find how many un-popped balloons remain after n balloons are inflated.
#  Every 4th balloon pops automatically.
# def balloons_left(n):
#     # write your code here
#     count=0
#     for i in range(1,n+1):
#         if i%4==0:
#             count+=1
#     remain_bal=n-count
#     print(remain_bal)

    

# """balloons_left(4)
# balloons_left(10)"""
# # balloons_left(20)



# # Write a function to calculate total savings after n months.
# #  The person saves ₹100 in the first month and increases savings by ₹50 every month.
# def total_savings(months):
#     # write your code here
#     for 
# total_savings(1)
# total_savings(3)
# total_savings(6)




# def fizzbuzz_game(n):
#     for i in  range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("fizzbuzz")
#         else:
#             print(i)
# fizzbuzz_game(15)

# def odd_num(n):
#     for  i in range(n+n,0,-1):
#         if i % 2 != 0:
#             print(i)
# odd_num(7)

# Given a number a check if its a multiple of 7 or not
# def num(a):
#     if a%7 == 0:
#         print("yes")
#     else:
#         print("not")
# num(13)
# num(14)
# num(70)
# num(21)

# You are given three numbers A, B & C. Print the largest amongst these three numbers.
# def num(a,b,c):
#     if a > b and a > c:
#         print(a)
#     elif b > c:
#         print(b)
#     else:
#         print(c)
# num(5,4,3)
# num(3,4,5)
# num(7,8,9)

# def num(a,b):
#     sum = a + b
#     if sum % 2 != 0:
#         print("odd")
#     else:
#         print("even")
# num(1,2)
# num(4,2)
# num(13,1)

# def num(n):
#     if n % 1 != 0 and n % n != 0:
#         print("not a prime")
#     else:
#         print("prime")
# num(15)
# def num(n):
#     for i in range(2,n):
#         print()
# def primenum(n):
#     count = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             count+=1
#     if count == 2:
#         print("prime")
#     else:
#         print("Not a prime")
# primenum(5)

# def num_list(n):
#     lists = list(str(n))
#     sum=0
#     for i in lists:
#         sum += int(i)
#     print(sum)
# num_list(1234)

# def add_num(n):
#     num = []
#     for i in range(1,n+1):
#         num.append(i)
#     print(num)
# add_num(5)

# def number(n):
#     num = []
#     for i in range(1,n+1):
#         if i % 2 != 0 and i % 7 == 0:
#             num.append(i)
#     print(sum(num))
# number(10)


# def add_num(n):
#     sum = 0 
#     num =list(str(n))
#     for i in num:
#         sum += int(i)
#     print(sum)
# add_num(1234)


# def list_num(n):
#     num = []
#     for i in range(1,n+1):
#         num.append(i)
#     print(num)
# list_num(5)

# def num(lists,b):
#     count = 0
#     for i in range(0,len(lists)):
#         if lists[i] == b:
#             count += 1
#     print(count)
# num([11,55,22,11,33,11,56,76,11],11)


# names = ['virat','dhoni','hardhik']
# scores = [99,72,60]
# for i in range(len(scores)):
#     if scores[i] > 70:
#         print(i)


# names = ['virat','dhoni','hardhik']
# scores = [99,72,60]
# for i in range(len(scores)):
#     if scores[i] > 70:
#         s =scores[i].index
#         print(s)
# for names in s:
#     print(names)

# vowels = ['a','e','i','o','u']
# sentence = "seriously"
# count = 0
# for i in sentence:
#     if i in vowels:
#         count+=1
# print(count,"Vowels")

# In the dictionary created. find the students who have scored more than PASS_MARK .


# name = ['kaiv','saran'']

# num = [2,3,4,5]
# n = 3
# m = []
# sums = 0
# for i in num:
#     if i > 3:
#         m.append(i)
#         sums += i
# print(sums)

# num = [1,2,3,4,5,6,7,8,9]
# for i in num:
#     if i % 2 != 0:
#         print(i)


# arr = [1,2,3,4,5,6]
# count  = 0
# for i in arr:
#     if i % 2 == 0:
#         count += 1
# print("even",count,"odd",len(arr)-count)


# arr = [1,5,2,3,4,5,7,8,0,5]
# tv = 5
# lists = 0
# count = 0
# for i in range(len(arr)):
#     if arr[i] == tv:
#         count = i
#         print(count)
#     count.append
#     print(count)

 

# arr = [1,2,0,3,4,5,6,7,9,8]
# start = 0
# end = 0
# res = []
# for i in range(len(arr)):
#     if arr[i] == 0:
#         start = i
#         break
# for j in range(len(arr)-1,-1,-1):
#     if arr[j] == 0:
#         end = j
#         break
# if start == end:
#     print("-1")
# else:
#     for k in range(len(arr)):
#         if k > start and k < end:
#             res.append(arr[k])
#     print(res)

# arr  = "united states america"
# space = " "
# res = []
# for i in range(len(arr)):
#     res.append(arr[i][0])
# if arr[i] == space:
#     res.extend(arr[i])
# print(res)


# arr = [1,2,3,4,5]
# count = 0
# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         count += 1
# print(count)
   
# arr = [4, 15, 9, 20, 2]
# res = 0
# for i in range(len(arr)):
#     if arr[i] > 10:
#         res += arr[i]
# print(res)


# arr = [1,2,3,4,5,6,7,8]
# maximum = arr[0]
# minimum = arr[0]
# for  i in range(len(arr)):
#     if arr[i] > maximum:
#         maximum = arr[i]
# for j in range(len(arr)):
#     if arr[j] < minimum:
#         minimum = arr[j]
# print(f"{minimum,maximum}")




# Count vowels in a string
# :point_right: Input: "hello world" → Output: 3

# arr = "amstrong"
# vowels = "aeiouAEIOU"
# count = 0
# for i in range(len(arr)):
#     if arr[i] in vowels:
#         count+=1
# print(count)

# Reverse each word in a string
# :point_right: Input: "hello world" → Output: "olleh dlrow"
# arr = "hello world"
# ans = []
# res = arr.split()
# for i in res:
#     ans.append(i[::-1])
# print(ans)


# Find length of each word
# :point_right: Input: "I love python" → Output: [1, 4, 6]

# arr = "i love  python".split()
# res = []
# count = 0
# for i in arr:
#     for j in i:
#         count += 1
#     res.append(count)
#     count = 0
# print(res)

# arr = [5,8,11,14]
# # res = 0
# # for i in arr:
# #     res += i
# # print(res)

# arr = [2,3,5,8,11,14,15]
# max = arr[0]
# min = arr[0]
# for  i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# for j in range(len(arr)):
#     if arr[j] < min:
#         min = arr[j]
# print(min,max)

# lists = ["ams","arun","ajay","bala","adhi"]
# for i in lists:
#      print(len(i),end=" ")




# arr = ["a","b","c","d","e"]
# ans = []
# for i in range(len(arr)-1,-1,-1):
#     ans.append(arr[i])
# print(ans)

# arr = [2,4,6,8,10]
# res = []
# for i in arr:
#     res.append(i*2)
# print(res)

# arr = [20,40,50,70,80,90]
# count = 0
# for i in arr:
#     if i > 50:
#         count += 1
# print(count)



# arr = [1,2,3,4,5,6,7]
# num = int(input("enter a number:"))
# for i  in range(len(arr)):
#     if arr[i] != num:

# arr = [1,1,2,3,4,5,5,6,6,8,9,9,7]
# lists = []
# for i in arr:
#     if i not in lists:
#         lists.append(i)
# print(lists)

# arr1 = [1,2,3,4]
# arr2 = [1,2,3,4]
# sum = []
# for i in range(len(arr1)):
#     sum.append(arr1[i] + arr2[i])
# print(sum)

# arr = "amstrong"
# vowels = "aeiouAEIOU"
# count = 0
# for i in arr:
#     if i in vowels:
#         count += 1
# print(count)

# arr = "amstrong"
# res = ""
# for i in range(len(arr)-1,-1,-1):
#     res += arr[i]
# print(res)

# arr = "anandh"
# strng = input("enter a character::").lower()
# count = 0
# for i in arr:
#     if i in strng:
#         count += 1
# print(count)

# arr = "m a  d a m"
# rev = ""
# strt = ""
# for i in range(len(arr)-1,-1,-1):
#     if arr[i] != " ":
#         rev += arr[i]
# for j in range(len(arr)):
#     if arr[j] != " ":
#         strt += arr[j]
# if strt == rev:
#     print("yes")
# else:
#     print("false")


# arr = "amstrong"
# count = 0
# for i in arr:
#     count += 1
# print(count)

# a= "hello world"
# res = ""
# ans = ""
# lists = list(a)
# for i in range(len(lists)):
#     if lists[i] == " ":
#         lists[i] = "-"
# print(lists)
# for i in lists:
#     res += i
#     res.split("-")
# print(res)

# a = "hello w ord"
# b = a.split(" ")
# print(b)
    
# arr = "i Love Python"
# up = "abcdefghijklmnopqrstuvwxyz"
# low = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# up_count = 0
# low_count =0

# for i in arr:
#     if i in up:
#         up_count += 1
# for j in arr:
#     if j in low:
#         low_count += 1
# print(up_count,low_count) 

# arr = "i love python love"
# lists = arr.split(" ")
# count = 0
# for i in lists:
#     count += 1
# print(count)

# arr  = "python"
# res = ""
# for i in range(len(arr)):
#     if i % 2 == 0:
#         res += arr[i]
# print(res)

# arr = "pyt2ho5n"
# num = "1234567890"
# lists = "abcdefghijklmnopqrstuvwxyz"
# res1 = ""
# res2 = ""
# for i in arr:
#     if i in num:
#         res1 += i
# for  j in arr:
#     if j in lists:
#         res2 += j
# print(res2)

# arr = "python"
# count = 0
# for i in arr:
#     count += 1
# print(count)


# arr1 = [1,2,3,4]
# arr2 = [1,2,3,4]
# sum = []
# for i in range(len(arr1)):
#     sum.append(arr1[i] + arr2[i])
# print(sum)
# arr = "python"
# res =""
# for i in range(len(arr)-2,0,-1):
#     res += arr[i]
# print(res)

# arr = "NorthAmerica"
# res = ""
# for i in arr:
#     if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != "A" and i != "E" and i != "I" and i != "O" and i != "U":
#         res += i
# print(res)

# str1 = "Amstrong".lower()
# str2 = "jesudas".lower()
# vowels = "aeiouAEIOU"
# count1 = 0
# count2 = 0
# for i in str1:
#     if i in vowels:
#         count1 += 1
# for j in str2:
#     if j in vowels:
#         count2 += 1
# if count1 < count2:
#     print(str1)
# elif count2 < count1:
#     print(str2)
# else:
#     print("no vowels")

# students = [
#     {"name": "Arun", "marks": 100},
#     {"name": "Priya", "marks": 88},
#     {"name": "Kiran", "marks": 1000}
# ]
# temp = students[0]["marks"]
# for i in range(len(students)):
#     if students[i]["marks"] > temp:
#         temp = students[i]["marks"]
# for j in range(len(students)):
#     if students[j]["marks"] == temp:
#         print(students[j]["name"])

# Given a list, find all numbers having 0 as last digit.
# Given a string, print if it has all the vowels


# arr = [10,15,13,20,350,1000]
# res = []
# for i in range(len(arr)):
#     if arr[i] % 10 == 0:
#         res.append(arr[i])
# print(res)


# arr = "education"
# temp = ["a","e","i","o","u"]
# count = 0
# for i in arr:
#     if i in temp:
#         temp.remove(i)
#         count += 1
# if temp == []:
#     print(arr)
# else:
#     print("only",count," vowels in your string")

# arr = ("education").lower()
# vowels = "aeiou"
# count = 0
# for i in vowels:
#     if i in arr:
#         count += 1
# if count  == 5:
#     print(arr)
# else:
#     print("no")

# arr = [10,20,30,40,50]
# for i in arr:
#     print(i)

# arr = [1,2,3,4,5,6,7,8,9]
# for i in arr:
#     if i % 2 != 0:
#         print(i,end=" ")

# arr = [1,2,3,4]
# sum = 0
# for i in arr:
#    sum += i
# print(sum)

# arr = [1,2,3,4,5,64,7,8,12]
# maximum = arr[0]
# for i in range(len(arr)):
#     if arr[i] > maximum:
#         maximum = arr[i]
# print(maximum)

# arr = [10,25,63,12,5,9,]
# count = 0
# for i in arr:
#     if i > 10:
#         count += 1
# print(count)

# arr = [1,2,3,4]
# res = []
# for i in arr:
#     res.append(i+5)
# print(res)

# arr = [0, 1, 0, 2, 3, 0]
# count = 0
# for i in arr:
#     if i == 0:
#         count += 1
# print(count)

# arr = [10, 20, 30, 40, 50]
# for i in range(len(arr)):
#     if i % 2 == 0:
#         print(arr[i],end=" ")

# list1 = [1, 2, 3, 4]
# list2 = [1, 5, 3, 7]

# for i in range(len(list1)):
#     if list1[i] in list2:
#         print(list1[i])

# string = "Python is fun"
# count = 0
# for i in string:
#     if i == " ":
#         count += 1
# print(count)

# string = "python"
# res = ""
# for i in range(len(string)):
#     if i % 2 == 0:
#         res += string[i]
# print(res)

# arr = "Education".lower()
# vowels = "aeiou"
# res = ""
# for i in arr:
#     if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
#         res += i
# print(res)

# arr = [10,20,2,23,4,5,6]
# maximum = arr[0]

# for i in range(len(arr)):
#     if arr[i] > maximum:
#         maximum = arr[i]
# print(maximum)

# def count_element(input_list,element):
#    count = 0
#    for i in input_list:
#       if i == element:
#          count += 1
#    print(count)

# count_element([1,2,3,5,4,5,6,7,5,7],5)

# list1 = [1,2,3,11,5,6,7]
# list2  = [2,3,4,11,5,8,96]
# temp = []
# for i in range(len(list1)):
#     if list1[i] in list2:
#         temp.append(list1[i])
# print(temp)           

# arr = [1,2,3,4,5,6,5,6,5]
# temp = []
# for i in range(len(arr)):
#     if arr[i] not in temp:
#         temp.append(arr[i])
# print(temp)

# arr = [1,7,3,4,5,6]
# arr2 = [1,2,3,4,5,6]
# if arr == arr2:
#     print("same")
# else:
#     print("no")

# arr = "A man, a plan, a canal: Panama"
# temp = ""
# temp2 = ""
# for i in range(len(arr)-1,-1,-1):
#     if arr[i] != " ":
#         temp += arr[i]
# print(temp)
# for  j in range(len(arr)):
#     if arr[j] != " ":
#         temp2 += arr[j]
# print(temp2)

# data_x = [1, 2, 3, 4, 5, 6, 7]
# data_y = [11, 22, 33, 44, 55]
# count1 = 0
# count2 = 0
# for i in  range(len(data_x)):
#     if data_x[i] % 2 != 0:
#         count1 += 1
# for j in range(len(data_y)):
#     if data_y[j] % 2 != 0:
#         count2 += 1
# if count1 > count2:
#     print(data_x)
# elif count2 > count1:
#     print(data_y)
# else:
#     print("both or equal odd number")

# arr = [1,3,4,5]
# strt = arr[0]
# for i in range(len(arr)):
#     if strt % 2 == 0:
#         if arr[i] % 2 != 0:
#             print(arr[i])
#     elif strt % 2 != 0:
#         if arr[i] % 2 == 0:
#             print(arr[i])

# human_resources = {'Alice', 'Bob', 'Charlie', 'David'}
# marketing = {'Charlie', 'Eve', 'Frank', 'David', 'Grace'}
# print(human_resources&marketing)

# num = "TN10A1015"
# res = 0
# for i in range(len(num)-1,len(num)-5,-1):
#     res+=int(num[i])
# print(res)


# arr = "13/7/1997"
# temp = arr.split("/")
# month = int(temp[1])
# if month > 0 and month <= 12:
#     print("yes")
# else:
#     print("no")



# s = "AC30BD40".lower()
# num = "1234567890"
# alpha  = "abcdefghijklmnopqrstuvwxyz"
# number = 0
# res = ""
# ans = ""
# for i  in range(len(s)):
#     if s[i] in num:
#         number +=int(s[i])
#     elif s[i] in alpha:
#         res += s[i]
#     ans =(res + str(number))
# print(ans)

# 1. Vehicle & Car
# Create a class Vehicle with:
# Attributes:
# brand
# price
# Methods:
# show_basic_info() → Print brand and price
# apply_discount(amount) → Reduce price by a given amount
# Create a subclass Car that adds:
# Attribute:
# fuel_type
# Methods:
# show_car_info() → Print brand, price, and fuel type
# update_fuel_type(new_type) → Change fuel_type
# Use super() inside the constructor to initialize brand and price.

# class vehicle():
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#         def show_basic_info(self):
#             print(self.brand,self,price)
#         def apply_discount()

# Level 3 Problems on Lists:
# ### LISTS
# - Given a list, rotate it right by k positions.
# ```python
# #test case 1:
# Input: nums = [4,6,9,2,3,11], k = 2
# Output: [3,11,4,6,9,2]

# nums = [4,6,9,2,3,11]
# k = 3
# for i in range(1,len(num)6,)

# for j in range(len(nums)):
#     if nums[j] not in res:
#         res.append(nums[j])
# print(res)


# res = []
# for i in range(len(nums)):
#     if i > k:
#         res.append(nums[i])
# for j in range(len(nums)):
#     if nums[j] not in res:
#         res.append(nums[j])
# print(res)

# nums = [4,2,7,2,9,3,2,8]
# k = 2
# res = []
# for i in range(len(nums)):
#     if nums[i] == k:
#         res.append(i)
# if nums[i] !=0:
#     print("not found")
# else:
#     print(res)

# nums = [4,2,7,2,9,3,2,8]
# res=[]
# for i in range(len(nums)-1,-1,-1):
#     res.append(nums[i])
# print(res)


# s = 0
# res1 = []
# for i in range(len(nums)):
#     if nums[i] == k:
#         s = i
# for j in range(len(nums)):
#     if j > s:
#         res1.append(nums[j])
# for l in range(len(nums)):
#     if nums[l] not in res1:
#         res1.append(nums[l])
# print(res1)

# - You are given a list of numbers and a target value.
#   Your task is to find all the indices at which the target value appears and PUT THOSE IN A NEW LIST.
# ```python
# #test case 1
# Input: nums = [4,2,7,2,9,3,2,8], k = 2
# Output: [1,3,6]
# #test case 2
# Input: nums = [10,55,17,29,3], k = -45
# Output: "Not Found"


# nums = [1,3,7,8,9]
# print(nums[::-1])



# - You are given a list of numbers and a target value.
#   Your task is to find all the indices at which the target value appears and PUT THOSE IN A NEW LIST.
# ```python
# #test case 1
# Input: nums = [4,2,7,2,9,3,2,8], k = 2
# Output: [1,3,6]
# #test case 2
# Input: nums = [10,55,17,29,3], k = -45
# Output: "Not Found"

# nums = [4,2,7,2,9,3,2,8]
# k = 2
# res = []
# for i in range(len(nums)):
#       if res == []:
#            print("not found")
#            break
#       elif nums[i] == k:
#          res.append(i)
# print(res)

# Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is

# arr = "Python is super powerful"
# res = arr.split()
# sn = len(res[0])
# for i in res:
#     if len(i) < sn:
#         sn = len(i)       
# for i in res:
#     if len(i)==sn:
#         print(i)

# 2. A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False (because 2 is NOT less than 2)
# [10,5,6] → False (because 5 < 10)

# 3. Reverse characters only at even index positions Indices: 0,2,4,6,...
# Input: "abcdefg" Even positioned letters: a, c, e, g → reverse → g, e, c, a
# Final Output: "gbecdfa"
# 4. Replace characters at odd indexes with *.
# Example: "hello" → "h*l*o" (edited) 

# arr = "abcdefgh"
# res = ""
# ans = ""
# for i in range(len(arr)-1,-1,-1):
#     if i % 2  == 0:
#         res += arr[i]
# print(res)


# nums = [2, 7, 11, 15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print([j,i])

# nums = [1,2,3,4]
# temp = []
# for i in range(len(nums)):
#     if nums[i] not in temp:
#         temp.append(nums[i])
# if len(temp) < len(nums):
#     print(True)
# else:
#     print(False)

# arr = [1,2,3,4,5,6,7,8,8,9]
# count = 0
# max = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#         count += 1
#         if count < 2:
#             arr.remove(max)
# print(max)


# def highest_avg(first_list, second_list) :
#     #Enter your code here
#     count1 = 0
#     count2 = 0
#     sum1 = 0
#     sum2 = 0
#     for i in range(len(first_list)):
#         count1 += 1
#         sum1 += first_list[i]
#     avg1 = sum1 / count1
#     for j in range(len(second_list)):
#         count2 += 1
#         sum2 += second_list[j]
#     avg2 = sum2 / count2
#     if avg1 > avg2:
#         print(first_list)
#     elif avg2 > avg1:
#         print(second_list)
#     elif avg1 == avg2:
#         print("Both are equal")

# highest_avg([4, 1, 2, 3, 5], [1, 0, 0, 1, 2, 1, 0, 2


# arr1 = [1,2,3,4,5,8,11,12,14]
# arr2 = [1,2,3,4,5,6,7]
# count1 = 0
# count2 = 0
# for i in range(len(arr1)):
#     if arr1[i] % 2 == 0:
#         count1 += 1
# for j in range(len(arr2)):
#     if arr2[j] % 2 == 0:
#         count2 += 1
# if count1 > count2:
#     print(arr1)
# elif count2 > count1:
#     print(arr2)



# Given a string "python" print all the characters in the even position, 
# taking the first position as 1 and print it in reverse

# arr = "helloworld
# res = ""
# for i in range(len(arr)):
#     if (i+1) % 2 == 0:
#         res += arr[i]
# print(res[::-1])


# alpha = input("enter alphapets:")
# temp = "abcdefghijklmnopqrstuvwxyz"
# res = ""
# for i in range(len(temp)):
#     if temp[i] in alpha:
#         res += temp[i]
# print(res)


# arr = [1,8,3,4,1,10]
# max = max(arr)
# min = min(arr)
# temp = []
# res = []
# for i in range(min,max+1,1):
#     temp.append(i)
# for j in range(len(temp)):
#     if temp[j] not in arr:
#         res.append(temp[j])
# print(res)


# books = [98, 75, 60, 50, 40, 25]
# newbook = 30

# for i in range(len(books)):
#     if books[i] < newbook:
#         print(i+1)
#         break
# else:
#     print(-1)


# word = "this is an Animal"
# words = word.split()
# print(words)
# vowels = "aeiouAEIOU"
# for i in range(len(words)):
#     if words[i][0] in vowels:
#         print(words[i])


# word = "john,80/manisha,60/syed,90/fiaz,30/amstrong,100/indhu,1200"
# temp = []
# spltwrd = word.split("/")

# print(spltwrd)
# splt2 = ",".join(spltwrd)
# print(splt2)

# splt3 = splt2.split(",")
# print(splt3)

# for i in range(len(splt3)):
#     if i % 2 != 0:
#         temp.append(int(splt3[i]))
# print(temp)

# max = temp[0]
# maximum = ""
# for i in range(len(temp)):
#     if temp[i] > max:
#         max =(temp[i])
#         maximum = str(max)
# print(maximum)

# for i in range(len(splt3)):
#     if splt3[i] == maximum:
#         print(splt3[i-1],maximum)


# word = "john,80/manisha,60/syed,90/fiaz,30/amstrong,100/indhu,1200"
# words = word.split("/")
# mark = 0
# name = ""
# for ch in words:
#     names,marks = ch.split(",")
#     mark = int(marks)
#     if marks > mark:
#         mark = marks
#         print(mark)


# word  = ["reboot","restart","uvicorn"]
# input = "r"
# for i in range(len(word)):
#     if word[i][0] == input:
#         print(word[i])

# input = [10,20,30,40,50]
# count = 0
# sum = 0
# count1 = 0
# for i in range(len(input)):
#     sum += input[i]
#     count += 1
# avg = sum/count

# for j in range(len(input)):
#     if input[j] > avg:
#         count1 += 1
# print(count1)

# input = 'programming'
# res = ""
# for i in input:
#     if i not in res:
#         res += i
# print(res)

# input = "Python makes programming  enjoyable"
# temp = input.split()
# max = len(temp[0])
# res = ""

# for i in range(len(temp)):
#     if len(temp[i]) > max:
#         max = len(temp[i])
#         res = temp[i]
# print(res


# lists = "data science evolves every year"
# l_words = lists.split()
# max = len(l_words[0])
# res = 


# for i in range(1,len(l_words)):
#     if len(l_words[i]) > max:
#         max = l_words[i]
# print(max)


# lst = "baeat moon aeiou programming  "
# word = lst.split(" ")
# vowel = "aeiouAEIOU"
# res = ""
# count1 = 0
# count2 = 0

# for i in word[0]:
#     if i in vowel:
#         count1 += 1
#         res 


# lst = "baeat moon aeiou programming"
# words = lst.split()
# vowels = "aeiouAEIOU"
# max = 0
# max_word =""

# for word in words:
#     count = 0
#     for ch in word:
#         if ch in vowels:
#             count += 1
#     if count > max:
#         max = count
#         max_word = word
# print(max_word)


# input = "AAc3@b55"
# number = "1234567890"
# alpha = "zxcvbnmasdfghjklqwertyuiopABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numcount = 0
# alphacount = 0
# othercount = 0


# for i in input:
#     if i in number:
#         numcount += 1
# for j in input:
#     if j in alpha:
#         alphacount += 1
# for k in input:
#     if k not in alpha and k not in number:
#         othercount += 1
# print(numcount,alphacount,othercount)


# input = [3, -2, 8, -5, 0]
# sum = 0
# for i in input:
#     if i < 0:
#         sum += i
# print(sum)


# input = [2, 3, 4]
# res = 0
# for i in range(len(input)):
#     for j in range(1,len(input)):
#         res = input[i] * input[j]


# arr =  ["ab12", "hello", "9nine", "cat"]
# number = "1234567890"

# for i in range(len(arr)):
#     for j in arr[i]:
#         if j in number:
#             print(arr[i])
#             break


# season = input("enter a season:")
# city = ["chennai", "trichy", "coimbatore", "bangalore", "salem"]
# summer  = [38, 40.0, 32.0, 30.0, 37.0]   
# monsoon = [30, 212.0, 28.0, 25.0, 29.0]   
# winter  = [25, 24.0, 20.0, 18.0, 23.0]


# data = {
#     "summer":summer,
#     "monsoon":monsoon,
#     "winter":winter
# }
# res = city[0]
# if season not in data:
#     print("invalid input")
# else:
#     sea = data[season]
#     max = sea[0]
#     for i in range(len(sea)):
#         if sea[i] > max:
#             max = sea[i]
#             res = city[i]
#     print(res)


# num = 123
# number = str(num)
# res = []
# for i in range(len(number)):
#     res.append(int(number[i]))
# print(res)

# arr = "iron man is flying"
# word = arr.split()

# for i in range(len(word)-1,-1,-1):
#     print(word[i],end=" ")

# arr = "Secret   mission   starts   now"
# words = arr.split()
# res = ""
# for i in words:
#     print(i,end=" ")

# Master_list = [10,20, 30,100,40, 50]
# Current_list = [40, 10, 20, 50]

# for i in Master_list:jothi
#     if i not in Current_list:
#         print(i)



# arr = "suresh"

# vowels = "aeiou"
# count = 0
# for i in arr:
#     if i in vowels:
#         count += 1
#         print(i,end="")
# print()


# Given a value of N print the below pattern (5 M)
# N = 3
#     *
#   * *
# * * *
#   * *
#     * 


n = 3

for


 




































        
            
    



































































































































































