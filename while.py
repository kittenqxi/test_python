# taks 1
# Ask the user to enter numbers one by one.
# Keep asking for numbers while the number is positive (greater than 0).
# Add all positive numbers together.
# When the user enters a number 0 or negative, stop the loop and print the total sum.
# Example:
# User inputs: 5, 3, 2, -1 → program prints sum = 10.


# task 2
# Ask the user to enter a number.
# Print each digit of the number one by one, starting from the last digit.
# Example:
# User types: 123
# Output should be:
# 3
# 2
# 1
#task 1
# num=int(input('Enter a number: '))
# total=0
# while num>0:
#     total+=num
#     num=int(input())
# print('sum = ', total)
#task 2
# num=int(input('Enter a number: '))
# if num<0:
#     num=abs(num)
# while num!=0:
#     l_d=num%10
#     print(l_d)
#     num-=l_d
#     num=num//10


# task 3
#  Find the first number > N that is divisible by 4, skipping all numbers that contain the digit 0
# User enters N (only integer)
# Using a while loop:
# If the number contains the digit 0 → continue.
# If it is divisible by 4 → break and print it.

# task 4
#  Find the first three-digit number whose digit sum is even, skipping all numbers divisible by 5
# Start from 100.
# If the number is divisible by 5 → continue.
# If the sum of its digits is even → break and print it.

# task 5
#  User enters numbers(only integer); ignore negative numbers (continue), stop when a number divisible by 13 appears
# Infinite input loop:
# If the number < 0 → continue.
# If number % 13 == 0 → break and print it.
# n=int(input())
# num=n+1
# while True:
#     s = str(num)
#     if '0' in s:
#         num+=1
#         continue
#     if num%4==0:
#         print(num)
#         break
#     num+=1
num=100
while True:
    if num%5==0:
        num+=1
        continue
    digit1=num//100
    digit2=(num//10)%10
    digit3=num%10
    sum=digit1+digit2+digit3
    if sum%2==0:
        break
    num+=1
print(num)