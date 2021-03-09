def time_conversion(number):
    hour = number // 60
    mins = (number % 60)
    time = hour + mins
    string_hour = str(hour)
    string_min = str(mins)
    if hour <= 1:
        print(string_hour + " " + "hour")
    else:
        print(string_hour + " " + "hours")
    if mins <= 1:
        print(string_min + " " + "minute")
    else:
        print(string_min + " " + "minutes")


time_conversion(63)
