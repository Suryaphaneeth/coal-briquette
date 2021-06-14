## all(list) - All function returns true if all the values in the list are true. 
def is_palindrome(s):
    return all(s[i] == s[-i] for i in range(len(s)//2))

val = input("Enter your string value: ")
print(is_palindrome(val))