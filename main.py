

def printMenu():
    """
    prints the UI
    """
    print("Alegeti o optiune de mai jos:")
    print("1. Citire lista(in aceeasi linie separate prin spatiu)")
    print("2. Afiseaza lista fara duplicate")
    print("3. Afiseaza suma primelor n numere naturale din lista")
    print("4. Verifica daca lista este sortata crescator")
    print("6.exit")

def readList():
    """
    takes the input from the user and returns a list of floats
    """
    lst = []
    inputs = input("Introduceti valorile listei: \n")
    for value in inputs.split():
        lst.append(int(value))
    return lst

def eliminateDuplicate(lst):
    """
    param lst: list of integers
    returns a list with unique elements of lst
    """
    uniqueList = []
    for value in lst:
        if value not in uniqueList:
            uniqueList.append(value)

    return uniqueList

def getSumFirstPoz(lst, n):
    """
    parameters: lst - list of integers
                n - int 
    returns first n positive numbers in lst
    """
    count = 0
    total = 0
    for value in lst:
        if value >= 0 and count < n:
            total = total + value
            count = count +1

    if count >= n:
        return total
    else:
        return "Dimensiunea listei este prea mica"

def checkIfLstIsAsc(lst):
    """
    parameter: lst - list of integers
    returns "DA" if the list is ascending, "NU" otherwise
    """
    newlist = []
    for value in lst:
        if value >= 0:
            newlist.append(value)

    if newlist == newlist.sort():
        return "DA"
    else:
        return "NU"

def testEliminateDuplicate():
    assert(eliminateDuplicate([3,4,2,4,3]) == [3,4,2] )
    assert(eliminateDuplicate([2,3,4]) == [2,3,4])
    assert(eliminateDuplicate([0,-3,-3]) == [0,-3])

def testGetSumFirstPoz():
    assert(getSumFirstPoz([2,3,4,-3],3) == 9)
    assert(getSumFirstPoz([-3,4], 2) == "Dimensiunea listei este prea mica")

def getIntegersFromList(lst):
    """
    parameter: lst: list of floats
    returns a list containing only the integers from lst
    """
    integerLst = []
    for i in lst:
        if i == int(i):
            integerLst.append(i)
    return integerLst

def getLargestDivisible(lst, number):
    """
    parameters: lst - list of floats
                number - float, the number we try to divide at
    returns the largest number in lst that is divisible with number
    """

    lst.sort(reverse=True)
    for value in lst:
        if value%number == 0:
            return value

    return None

def getFloatsWithFractionalPalindrom(lst):
    """
    parameters: lst - list of floats
    returns a sublist of lst that contains all elements of lst with the 
            fractional part a palindorm 
    """
    fracLst = []

    for value in lst:
        fraction = str(value).split(".")[1]
        if fraction == fraction[::-1]:
            fracLst.append(value)
    return fracLst

def testGetIntegersFromList():
    assert getIntegersFromList([2.0,3.0,4.0,5.3,7.2]) == [2.0,3.0,4.0]
    assert getIntegersFromList([]) == []
    assert getIntegersFromList([2.3,3.6]) == []

def testGetLargestDivisible():
    assert getLargestDivisible([3.5,4.5,5.0,3.0],1.5) == 4.5
    assert getLargestDivisible([3.0,2.2], 1.5) == 3
    assert getLargestDivisible([3.4,2.2], 1.5) == None
    assert getLargestDivisible([], 2) == None

def testGetFloatsWithFractionalPalindrom():
    assert getFloatsWithFractionalPalindrom([2.121,3.1,4.0,4.32]) == [2.121,3.1,4.0]
    assert getFloatsWithFractionalPalindrom([2.32,3.45]) == []
    assert getFloatsWithFractionalPalindrom([]) == []
    assert getFloatsWithFractionalPalindrom([1.1]) == [1.1]

def run():
    testEliminateDuplicate()
    testGetSumFirstPoz()
    lst=[]
    while True:
        print(f"Lista citita: {lst}")
        printMenu()
        option = input("optiune: ")
        if option == "1":
            lst = readList()
            lst = eliminateDuplicate(lst)
        elif option == "2":
            print(eliminateDuplicate(lst))
        elif option == "3":
            x = int(input("Introduceti valoarea lui x: "))
            print(getSumFirstPoz(lst, x))
        elif option == "4":
            print(checkIfLstIsAsc(lst))
        elif option == "6":
            break
        else:
            print("Optiune invalida")

if __name__ == "__main__":
    run()
