"""string"""
#Assume s is a string of lower case charas.
def main():
    """string"""
    str_ = input()
    coun_ = 0
    for char in str_:
        if char in ('a', 'e', 'i', 'o', 'u'):
            coun_ = coun_ + 1
    print(coun_)
if __name__ == "__main__":
    main()
