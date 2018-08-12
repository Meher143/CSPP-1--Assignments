# Assignment-3
'''
'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    for i in word:
    	if i not in hand:
    		return False
    return word in wordList

    


def main():
	word=input()
	n=int(input())
	adict={}
	for i in range(n):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	l2=input().split()
	print(isValidWord(word,adict,l2))
		


if __name__== "__main__":
	main()