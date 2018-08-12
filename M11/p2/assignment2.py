"""Exercise: Assignment-2"""
def update_hand(hand, word):
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
    """this is main"""
    number_ = input()
    adict = {}
    for i in range(int(number_)):
        data = input()
        list_1 = data.split()
        adict[list_1[0]] = int(list_1[1])
        i += 1
    data1 = input()
    print(update_hand(adict, data1))


if __name__ == "__main__":
    main()
