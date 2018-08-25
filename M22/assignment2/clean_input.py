'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''removing special characters '''
    string_1 = ""
    for i in string_1:
        if i in "!@#$%^&*( )_.' '+":
            letter = " "
            string_1 += letter
        else:
            string_1 += letter
    return string_1

def main():
    '''clean string'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
