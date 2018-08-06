'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
''' '''
def main():
    ''' '''
    Read any number from the input, store it in variable int_input.
    '''
int_input = int(input(""))
S = 1
while int_input> 0:
    N1 = int_input%10
    S = S*N1
    int_input= int_input//10
print(S)
if __name__ == "__main__":
    main()
