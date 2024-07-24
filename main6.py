while True:
    str1 = input("enter the first word: ")
    str2 = input("enter the first word: ")

    if str1 == str2:
        print(f"The words are identical : {str1}")
        break
    else:
        print(f"Concatenation of the words: {str1} {str2}")