'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    def eachline(data1):
        if "follows" not in data1:
            dic = {}
            return dic
        string_1 = data1.split(" follows ")
        list1 = []
        list1.append(string_1[0])
        string_1.remove(string_1[0])
        value = string-1[0].split(",")
        list1.append(value)
        
    l_1 = data.splitlines()
    #print("split",splitline)
    list_key = []
    list_value = []
    dic = {}
    for i in l_1:
        list_key_val = eachline(i)
        if list_key_val == dic:
            return list_key_val
        list_key.append(list_key_val[0])
        list_value.append(list_key_val[1])
    dictionary = dict(zip(list_key, list_value))
    return dictionary




def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    #print(string)
    print(create_social_network(string))

if __name__ == "__main__":
    main()
