numID = "123456782"


def makelist(numid):
    numlist = [int(digit) for digit in numid]  # Convert numid characters to integers
    listwithnums = numlist.copy()  # Make a copy of numlist

    for i in range(0, len(listwithnums)-1):
        if listwithnums[i] % 2 == 0:
            listwithnums[i] *= 2
        else:
            listwithnums[i] *= 1  # This line is not necessary since multiplying by 1 doesn't change the value

    listwithmulti = listwithnums  # Assign the modified listwithnums to listwithmulti

    return listwithmulti


result_list = makelist(numID)
print(result_list)
