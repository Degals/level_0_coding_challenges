def vowel_grab(string):
    string = string.lower()
    print("Vowels: ", end="")
    for vowel in "aeiou":
        if vowel in string:
            print(vowel, end=",")


vowel_grab("sennheiser")
