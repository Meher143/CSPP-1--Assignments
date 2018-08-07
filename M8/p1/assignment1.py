# Exercise: Assignment-1
'''This function takes in one number and returns one number.'''


def factorial(n_1):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_1 == 1:
        return 1
    return n_1*factorial(n_1 - 1)
def main():
    """ finding factorial"""
    a_1 = input()
    print(factorial(int(a_1)))

if __name__ == "__main__":
    main()
