def vowel_grab(string):
    string = string.lower()
    for vowel in "aeiou":
        if vowel in string:
            print(vowel)


vowel_grab("sennheiser")
