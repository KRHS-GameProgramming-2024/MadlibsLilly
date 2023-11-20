import os
def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False

    while not goodInput:
        option = input("please select an option ")
        option = option.lower ()

        if (option == "q" or 
        option == "quit" or 
        option == "x" or 
        option == "exit"):
            option = "q"
            goodInput = True

        elif (option == "1" or 
        option == "one" or 
        option == "story 1" or
        option == "story1"):
            option = "1"
            goodInput = True

        elif (option == "2" or
        option == "two" or
        option == "story 2" or
        option == "story2"):
            option = "2"
            goodInput = True

        else:
            print("please make a valid choice")

        return option


def getWord(promt, debug = False):
    if debug: print("getWord Function")

    goodInput = False

    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("don't use language like that")
        elif word == ("blue"):
            os.system("color 03")
            goodInput = False
    return word

def getPlace(promt, debug = False):
    if debug: print("getPlace Function")

    goodInput = False

    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("don't use language like that")

        elif word not in Place:
            goodInput = False
            print ("please pick one of the options available")


    return word
    
def getPlaceMenu(promt, debug = False):
    if debug: print("getPlace Function")

    goodInput = False
    promt += "\n\n"
    for i, p in enumerate(Place):
        promt += str(i + 1) + ".) " + p + "\n"
    promt+="> "
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("\ndon't use language like that")
        elif word.lower() not in Place:
            try:
                if int(word) <= len(Place):
                    word = Place[int(word) - 1]
                else:
                    goodInput = False
                    print ("\nplease pick one of the options available")
            except:
                goodInput = False
                print ("\nplease pick one of the options available")
        


    return word

def getSaidMenu(promt, debug = False):
    if debug: print("getPlace Function")

    goodInput = False
    promt += "\n\n"
    for i, p in enumerate(saidList):
        promt += str(i + 1) + ".) " + p + "\n"
    promt+="> "
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("\ndon't use language like that")
        elif word.lower() not in saidList:
            try:
                if int(word) <= len(Place):
                    word = saidList[int(word) - 1]
                else:
                    goodInput = False
                    print ("\nplease pick one of the options available")
            except:
                goodInput = False
                print ("\nplease pick one of the options available")
        
 

    return word
    
def getFruit (promt, debug = False):
    if debug: print("getFruit Function")

    goodInput = False

    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("don't use language like that")

        elif word not in fruitList:
            goodInput = False
            print ("I don't know that one,")
    return word

def getChip (promt, debug = False):
    if debug: print("getChip Function")

    goodInput = False

    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("don't use language like that")

        elif word not in chipList:
            goodInput = False
            print ("I don't know that one")
    return word

def getTime (promt, debug = False):
    if debug: print("getTime Function")

    goodInput = False

    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("don't use language like that")

        elif word not in Time:
            goodInput = False
            print ("please pick sunrise, morning, midmorning, noon, afternoon, sunset, night or midnight")
    return word

def isSwear(word, debug = False):
    if debug: print ("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False
swearList = ["poop",
 "pee",
 "bitch",
 "shit",
 "fuck",
 "piss",
 "dick",
 "cock",
 "ass",
 "pussy"]
Place = ["swamp",
 "mountain",
 "beach",
 "woods",
 "jungle",
 "desert",
 "city"]
fruitList = ["apple",
 "pear",
 "peach",
 "grapes",
 "watermelon",
 "cantalope",
 "orange",
 "lemon",
 "durian",
 "banana",
 "apples",
 "pears",
 "peaches",
 "watermelons",
 "cantalopes",
 "oranges",
 "lemons",
 "durians",
 "bananas",]
chipList = ["tortilla",
    "chip",
    "chips",
    "doritos",
    "lays",
    "barbecue chips",
    "bbq chips",
    "sour cream and onion chips",
    "sour cream & onion chips",
    "salt and vineger chips",
    "salt & vineger chips",
    "sun chips",]
Time = [ "sunrise",
    "morning",
    "midmorning",
    "noon", 
    "afternoon",
    "sunset",
    "night",
    "midnight",]
saidList = [ "said",
    "told",
    "stated",
    "explained",
    "affirmed",
    "lamented", ]
