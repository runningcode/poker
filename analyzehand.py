from evalutehand import evaluate, suit, values
import collections



def whatwedo(hand):
    howsit = evaluate(hand)
    if howsit[0] >= 4:
        return [] # do nothing.
    if howsit[0] == 3:
        return all_not(hand,howsit[1])
    if howsit[0] == 2:
        return all_not(hand,howsit[1])
    if howsit[0] == 1:
        return all_not(hand,howsit[1])

    closesuit = we_have_almost_flush(hand)
    if closesuit:
        return all_not_suit(hand,[closesuit])

    return three_lowest_cards(hand)


def we_have_almost_flush(hand):
    suits = suit(hand)
    print suits
    counts = collections.Counter(suits)
    for key,val in counts.iteritems():
        if val >= 4:
            return key
    return False


def three_lowest_cards(hand):
    return [1,2,3] ## PLEASE CHANGE THIS SOON


cardmap = {
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"T",
        11:"J",
        12:"Q",
        13:"K",
        14:"A",
}

def all_not(hand,vals):
    strvals = [cardmap[v] for v in vals]
    ziphand = zip(hand,range(1,6))
    print ziphand
    print hand
    print "doop"
    return [x[1] for x in ziphand if  x[0][0] not in strvals]

def all_not_suit(hand,vals):
    strvals = vals 
    ziphand = zip(hand,range(1,6))
    return [x[1] for x in ziphand if  x[0][1] not in strvals]

if __name__ == "__main__":
    print "asdf: "+str(evaluate(["ah","4h","2h","6h","3h"]))
    print "astf: "+str(whatwedo(["ah","4h","2h","6h","3h"]))
    print "asdf: "+str(whatwedo(["ah","4h","6h","6c","6h"]))
    print "asdf: "+str(whatwedo(["ah","4h","4h","6c","6h"]))
    print "asdf: "+str(whatwedo(["ah","3h","4h","6c","6h"]))
    print "asdf: "+str(whatwedo(["ah","3h","4h","8c","6h"]))