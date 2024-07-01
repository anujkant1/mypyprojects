"""
Define if a string is palindrome
"""

print("Enter a string:")
my_str = input("> ")

# half_way = int(len(my_str)/2)
# end_str = -1
# 
# for i in range(half_way):
#     if my_str[i] == my_str[end_str]:
#         end_str -= 1
#         continue
#     print("Not a palindrome")
#     break

def palindrome(my_str) -> bool:
    my_str = my_str.lower().replace(' ', '')
    return my_str == my_str[::-1]

print(palindrome(my_str))