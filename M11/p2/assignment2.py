#Exercise: Assignment-2
#Implement the updateHand function. Make sure this function has no side effects: i.e., it must not mutate the hand passed in. Before pasting your function definition here, be sure you've passed the appropriate tests in test_ps4a.py.


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    meher_1 = hand
    for i in word:
        if i in hand:
            meher_1[i] = meher_1[i] - 1
    return meher_1
    

def main():
    n_1=input()
    adict={}
    for i in range(int(n_1)):
        data=input()
        l_1=data.split()
        adict[l[0]]=int(l_1[1])
    data1=input()
    print(updateHand(adict,data1))
        


if __name__== "__main__":
    main()