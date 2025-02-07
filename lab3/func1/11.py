def pal():
    word = input()
    word = word.lower()
    comp = word[::-1]
    if word == comp:
        print("Palindrome")
    else:
        print("Not palindrome")
pal() 