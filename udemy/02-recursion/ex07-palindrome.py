def isPalindrome(str):
    if len(str) <= 1:
        return True
    elif str[0] != str[-1]:
        return False
    else:
        return isPalindrome(str[1:-1])


if __name__ == "__main__":
    str = "awesome"
    print(f"isPalindrome({str}) ? {isPalindrome(str)}")
    str = "tacocat"
    print(f"isPalindrome({str}) ? {isPalindrome(str)}")
    str = "amanaplanacanalpanama"
    print(f"isPalindrome({str}) ? {isPalindrome(str)}")
    str = "a"
    print(f"isPalindrome({str}) ? {isPalindrome(str)}")
