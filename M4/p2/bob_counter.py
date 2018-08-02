'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    """string"""
    str_ = input()
    coun_ = 0
    while str_ is "bob":
        coun_ = coun_+1
    print(coun_)
if __name__== "__main__":
	main()