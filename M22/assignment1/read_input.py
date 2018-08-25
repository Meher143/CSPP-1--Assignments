'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    string_1 = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string_1 += input()
        string_1 += '\n'
        print(string_1)
    

if __name__ == '__main__':
    main()
