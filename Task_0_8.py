def time_conversion(number):
    hour = number // 60
    mins = (number % 60)
    string_hour = str(hour)
    string_min = str(mins)
    if hour <= 1:
        print(string_hour + " " + "hour", ",", " ", end="")
    else:
        print(string_hour + " " + "hours", ",", " ", end="")
    if mins <= 1:
        print(string_min + " " + "minute", end="")
    else:
        print(string_min + " " + "minutes", end="")


time_conversion(63)
