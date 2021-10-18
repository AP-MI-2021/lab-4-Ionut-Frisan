

def printMenu():
    """
    prints the UI
    """
    print("Alegeti o optiune de mai jos:")
    print("a. Citire lista(in aceeasi linie separate prin spatiu)")
    print("1. Afiseaza toate numerele intregi din lista citita")
    print("2. Afiseaza cel mai mare numar divizibil cu numarul x citit de la tastatura")

def readList():
    """
    takes the input from the user and returns a list of floats
    """
    lst = []
    inputs = input("Introduceti valorile listei: \n")
    for value in inputs.split():
        lst.append(float(value))
    return lst

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
    testGetIntegersFromList()
    testGetLargestDivisible()
    testGetFloatsWithFractionalPalindrom
    lst=[]
    while True:
        print(f"Lista citita: {lst}")
        printMenu()
        option = input("optiune: ")
        if option == "a":
            lst = readList()
        elif option == "1":
            print(getIntegersFromList(lst))
        elif option == "2":
            x = int(input("Introduceti valoarea lui x: "))
            print(getLargestDivisible(lst, x))
        elif option == "3":
            print(getFloatsWithFractionalPalindrom(lst))
        else:
            print("Optiune invalida")

if __name__ == "__main__":
    run()
