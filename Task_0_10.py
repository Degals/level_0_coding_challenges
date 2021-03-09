def comparison_func(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    for letters in string1 and string2:
        if letters in string1 and string2:
            print(letters)


comparison_func("house", "computers")
