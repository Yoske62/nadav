from random import randint

def generateID():
    range_start = 10 ** (9 - 1)
    range_end = (10 ** 9) - 1

    while (True):
        id = randint(range_start, range_end)

        if (validateID(id)):
            return id

def validateID( id: int):
    validateDigit = id % 10
    numStep1 = id // 10
    sum = 0
    counter = 0

    while numStep1 > 0:
        counter += 1
        currDigit = numStep1 % 10
        numStep1 = numStep1 // 10
        numToAdd = 0

        if (counter % 2 == 0):
            numToAdd = currDigit
        else:
            numToAdd = currDigit * 2

        if (numToAdd > 9):
            sum += numToAdd % 10
            numToAdd = numToAdd // 10

        sum += numToAdd

    if (sum % 10 == 0):
        return validateDigit == 0
    else:
        return ((sum % 10) + validateDigit) == 10