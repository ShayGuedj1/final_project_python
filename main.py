numID = "123456782"

def makelist(num):
    numlist = [int(digit) for digit in num]  # Convert numid characters to integers
    print(numlist)
    listwithnums = numlist.copy()  # Make a copy of numlist

    for i in range(0, len(listwithnums)-1):
        if listwithnums[i] % 2 == 0:
            listwithnums[i] *= 2
        else:
            listwithnums[i] *= 1  # This line is not necessary since multiplying by 1 doesn't change the value. Easier to read
    listwithmulti = listwithnums  # Assign the modified listwithnums to listwithmulti
    print(listwithmulti)

    for i in range(0, len(listwithmulti) - 1):
        if listwithmulti[i] > 9:
            listwithmulti[i] = listwithmulti[i] - 10 + 1  # This calculates if the num is >= 10
        else:
            listwithmulti[i] = listwithmulti[i]
    listcalc = listwithmulti  # Assign the modified listwithmulti to listcalc
    print(listcalc)

    total = 0  # This is the first value of the total before calculating
    for i in range(0, len(listcalc)):

        total = total + listcalc[i]  # The var "total" receives each number and adds to the total
    print(total)








makelist(numID)
