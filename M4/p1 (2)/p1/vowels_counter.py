#Assume s is a string of lower case charas.


#Number of vowels: 5
def main():
    """string"""
    s = input()
    c = 0
    for char in s:
        if(char[s] == 'a','e','i','o','u'):
            c = c+1
    print(c)

if __name__ == "__main__":
	main()
