# 5-2. More Conditional Tests: You don't have to limit the number of tests you cre- ate to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
#   Tests for equality and inequality with strings
#   Tests using the lower() method
#   Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#   Tests using the and keyword and the or keyword
#   Test whether an item is in a list
#   Test whether an item is not in a list


# Tests for equality and inequality with strings
str1 = 'hello'
str2 = 'world'

print("\nIs 'hello' equal to 'world'? I predict False.")
print(str1 == str2)

print("\nIs 'hello' not equal to 'world'? I predict True.")
print(str1 != str2)

# Tests using the lower() method
word1 = 'PYTHON'
word2 = 'python'

print("\nIs 'PYTHON' equal to 'python' (case-insensitive)? I predict True.")
print(word1.lower() == word2.lower())

# Numerical tests
num1 = 10
num2 = 20

print("\nIs 10 greater than 20? I predict False.")
print(num1 > num2)

print("\nIs 10 less than 20? I predict True.")
print(num1 < num2)

print("\nIs 10 greater than or equal to 10? I predict True.")
print(num1 >= 10)

print("\nIs 20 less than or equal to 20? I predict True.")
print(num2 <= 20)

# Tests using the and keyword and the or keyword
age = 25
has_license = True

print("\nIs the person older than 18 and has a driver's license? I predict True.")
print(age > 18 and has_license)

print("\nIs the person younger than 18 or has a driver's license? I predict True.")
print(age < 18 or has_license)

# Test whether an item is in a list
fruits = ['apple', 'banana', 'cherry']

print("\nIs 'banana' in the list of fruits? I predict True.")
print('banana' in fruits)

# Test whether an item is not in a list
colors = ['red', 'green', 'blue']

print("\nIs 'yellow' not in the list of colors? I predict True.")
print('yellow' not in colors)
