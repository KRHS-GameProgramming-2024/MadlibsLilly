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
            option = "1"
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

def getFruit (prompt, debug = False):
    if debug: print ("getFruit Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("don't use language like that")
        elif word not in fruitList:
            gooodInput = False
            print ("I don't know that one")
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
 "beach", "woods", 
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

