
def longest_str(text):

    string = max(text, key=len)
    return string


str1=['cat', 'car', 'fear', 'center']

str2=['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

print(longest_str(str1))
print(longest_str(str2))
