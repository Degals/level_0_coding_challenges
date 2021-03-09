def maximum(int1, int2, int3):
    if int1 > int2:
        return int1
    elif int1 > int3:
        return int1
    elif int2 > int3:
        return int2
    else:
        return int3


def maximum_2(int1, int2, int3, int4):  # add int.. to parameter and edd elif int.. argument to function
    if int1 > int2:
        return int1
    elif int1 > int3:
        return int1
    elif int2 > int3:
        return int2
    elif int4 > int3:
        return int4
    else:
        return int3
