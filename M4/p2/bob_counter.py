"""string"""
def main():
    """string"""
    str0 = input()
    str1_ = 'bob'
    coun_ = 0
   	for i in range(len(str0)-2):
       	if str1_ == str0[i]+ str0[i+1]+str0[i+2]:
   	   	    coun_ = coun_+1
   	print(coun_)
if __name__== "__main__":
    main()