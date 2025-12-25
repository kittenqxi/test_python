# 1. Count vowels

# Description:
# Given a string, iterate through each character and count how many vowels it contains.
# Vowels are: a, e, i, o, u (case-insensitive).
# Do not use built-in methods like count() for each vowel.

# 2. Check string length

# Description:
# Given a string, check its length.

# If the length is greater than 10, print "long".

# Otherwise, print "short".

# 3. Replace spaces

# Description:
# Given a string, replace every space character (' ') with an underscore ('_').
# Build the result manually using a loop.

# 4. First and last character

# Description:
# Given a string:

# If the string is empty, print "Empty string".

# Otherwise, print the first and last characters.

# 5. Count digits

# Description:
# Given a string, count how many characters are digits (0–9).
# You may use comparisons or isdigit(), but not regular expressions.

# 6. Starts with capital letter

# Description:
# Check whether the first character of the string is an uppercase English letter (A–Z).
# If the string is empty, return False.

# 7. Reverse string (loop)

# Description:
# Reverse the string using a loop (for or while).
# Do not use slicing ([::-1]) or reversed().

# 8. Remove exclamation marks

# Description:
# Given a string, remove all ! characters and print the cleaned string.

# 9. Count specific letter

# Description:
# Count how many times the lowercase letter 'a' appears in the string.
# The comparison should be case-sensitive ('A' does not count).

# 10. Simple palindrome check

# Description:
# Check whether the string reads the same forward and backward.

# Case-sensitive

# No need to remove spaces or punctuation


# 11. Count words

# Description:
# Count how many words are in the string.
# A word is a sequence of characters separated by one or more spaces.
# Leading and trailing spaces should be ignored.

# 12. String compression

# Description:
# Compress the string by replacing consecutive repeating characters with the character followed by the count.
# Example:
# "aaabbc" → "a3b2c1"
# Use loops and conditions only.

# 13. Remove duplicate characters

# Description:
# Remove duplicate characters from the string, keeping only the first occurrence of each character and preserving order.
# Example:
# "banana" → "ban"

# 14. Find longest word

# Description:
# Given a sentence, find and print the longest word.
# If there are multiple words with the same maximum length, print the first one.

# 15. Alternate case

# Description:
# Convert the string so that:

# Characters at even indices are uppercase

# Characters at odd indices are lowercase
# Example:
# "python" → "PyThOn"

# 16. Check anagram

# Description:
# Given two strings, check if they are anagrams (contain the same characters in the same quantity).

# Case-sensitive

# Ignore spaces

# Do not use sorted()

# 17. Character frequency

# Description:
# Create a dictionary where keys are characters from the string and values are how many times each character appears.
# Do not use collections.Counter.

# 18. Remove extra spaces

# Description:
# Remove extra spaces so that:

# There is exactly one space between words

# No spaces at the beginning or end
# Do not use split() and join() together.

# 19. Most frequent character

# Description:
# Find the character that appears most frequently in the string.
# If multiple characters have the same maximum frequency, return the first one.

# 20. Manual split

# Description:
# Split the string into a list of words without using split().
# Words are separated by one or more spaces.
# Return a list of words.

#Task number one
# s=input()
# vowels=('aeiouAEIOU')
# vowel_counter=0
# for i in s:
#     if i in vowels:
#         vowel_counter+=1
# print(vowel_counter)

#task number two
# s=input()
# length=len(s)
# if length>10:
#     print('long')
# else:
#     print('short')

# #task number three
# s=input()
# result_s=''
# for i in s:
#     if i==' ':
#         result_s+='_'
#     else:
#         result_s+=i
# print(result_s)

#task number four
s=input()
if len(s)==0:
    print('Empty string')
else:
    first_character=s[0]
    last_character=s[-1]
    print(first_character, last_character)