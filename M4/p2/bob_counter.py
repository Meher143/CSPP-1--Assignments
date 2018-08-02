"""string"""
def main():
    """string"""
    str0_ = input()
    str1_ = 'bob'
    coun_ = 0
   	for i in range(len(str0_)-2):
       	if str1_ == str0_[i]+ str0_[i+1]+str0_[i+2]:
   	   	    coun_ = coun_+1
   	print(coun_)
if __name__== "__main__":
    main()