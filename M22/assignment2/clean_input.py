'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    words = []
    str1 = ''
    str2 = ""
    doc = [i.lower() for i in doc]
    for i in doc:
        k = i.split(" ")
        str2 = ''
        for j in k:
            str1 = ''
            for temp in j:
                if temp.isalpha() == False:
                    temp = ''
                str1 = str1 + temp
            str2 = str2 + str1 + " "
        words.append(str2)
    return words

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
