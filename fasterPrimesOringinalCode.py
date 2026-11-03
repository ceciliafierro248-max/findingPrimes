def allPrimesUpTo(num):
    primesFound = [2]
    for number in range(3, num + 1):
        for items in primesFound:
            if number % items == 0:
                break
        else:
            primesFound.append(number)
    noDuplicateList = list(dict.fromekeys(primesFound))
    return noDuplicateList
