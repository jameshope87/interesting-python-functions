
def is_palindrome(s):
    if s == '':
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

 
 
 
 
print(is_palindrome(''))
#>>> True
print(is_palindrome('abab'))
#>>> False
print(is_palindrome('abba'))
#>>> True
