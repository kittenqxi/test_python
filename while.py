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
num=int(input('Enter a number: '))
while num!=0:
    l_d=num%10
    print(l_d)
    num-=l_d
    num=num//10


