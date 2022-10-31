def isPalindrome(s):
    s = s.lower().replace(' ', '')  # this allows working on sentences as well
    if s == '' or len(s) == 1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]
        return isPalindrome(s)  # note: we might delete s = s[1:-1] and write directly return isPalindrome(s[1:-1])


def main():
    word = input('Enter a string: ')
    print('Is that a Palindrome?')
    if isPalindrome(word):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
