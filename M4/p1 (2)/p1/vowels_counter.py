#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	s = input()
	count=0
	for char in s:
		if(char[s]=='a' or char[s]=='e' or char[s]=='i' or char[s]=='o' or char[s]=='u'):
			count=count+1
	print(count)

if _name_=="_main_":
	main()
