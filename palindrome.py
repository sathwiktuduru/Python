# def palindrome(number):
#     if number == number[::-1]:
#         return True
#     return False
    
# def main():
#     n=input("Enter the string: ")
#     if palindrome(n):
#         print(f"{n} is palindrome")
#     else:
#         print("Not a palindrome")
        
# main()

# this is    sathwik

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    sentence=input("Enter the sentence: ")
    word=""
    for i in range(0, len(sentence)):
        if sentence[i]!=" ":
            word= word + sentence[i]
        elif sentence[i]==" ":
            word_check=palindrome(word)
            if word_check:
                print(f"{word} is Palindrome")
            else:
                print(f"{word} is not a palindrome")
            word=""
            continue
    word_check=palindrome(word)
    if word_check:
        print(f"{word} is Palindrome")
    else:
        print(f"{word} is not a palindrome")        
     
main()