def maximum(*numbers):
    largest_number = numbers[0]
    for integer in numbers:
        if integer > largest_number:
            largest_number = integer
    return largest_number


maximum(41800, 92, 3, 98000, 100)
