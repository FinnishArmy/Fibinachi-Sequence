def fib(n):
    """
    Inputs a number,
    Returns None if number is negative
    Otherwise return final fibinachi number in sequence
    Must use recursion
    """

    #If n is less than or equal to 0, return an error.

    if n < 0:
        return None

    #If n is equal to 0, return 0.

    if n == 0:
        return 0

    #If n is equal to 1, return 1.

    elif n == 1:
        return 1

    #If n is equal to 2, return 1.

    elif n == 2:
        return 1

    #If n is something else, return the fibinachi number.

    else:
        return(fib(n-1) + fib(n-2))

    #Tests if 1 equals 1.

def test1():
        if fib(1) == 1:
            print('1 Does give 1')

        else:
            print('That is not correct')

test1()

    #Tests if 0 equals 0.

def test0():
        if fib(0) == 0:
            print('0 Does give 0')

        else:
            print('That is not correct')

test0()

    #Tests if a negative number gives None.

def testNegative():
        if fib(-15) == None:
            print('-15 Is Nothing')

        else:
            print('-15 Should be nothing')

testNegative()

    #Test if 8 is equal to 21.

def test8():
        if fib(8) == 21:
            print('8 Does give 21')

        else:
            print('That is not correct')

test8()
