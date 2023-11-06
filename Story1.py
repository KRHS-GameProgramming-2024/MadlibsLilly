from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print ("    ")
    catName1 = getWord("Enter a name: ", debug)

    print ("      ")
    place1 = getPlace("Pick one, jungle, woods, mountain, beach, swamp, desert, or city: ", debug)

    print ("     ")
    duckName = getWord ("Enter a name: ", debug)

    print ("    ")
    fruitName1 = getFruit ("Enter a fruit: ", debug)

    print ("    ")
    fruitName2 = getFruit ("Enter another fruit: ", debug)

    print ("    ")
    verb1 = getWord ("Enter a verb: ", debug)

    print ("    ")
    verb2 = getWord ("Enter another verb: ", debug)

    print ("   ")
    birdname1 = getWord ("Enter a name: ", debug)

    print ("   ")
    Time1 = getTime ("Enter a time of day: ", debug)

    out = ""
    out += "    once a cat named " + catName1
    out += " went exploring the " + place1
    out += " when he saw a duck named " + duckName
    out += ". " + duckName
    out += " asked " + catName1
    out += " for help finding some fruit for a salad, he said yes and together to set off outside the " + place1
    out += " to find some " + fruitName1
    out += ". when they found the " + fruitName1
    out += ", they " + verb1
    out += " back to the " + place1 
    out += " where the duck lived and started making the fruit salad. They were almost done when they finished the cat realized that there was no " + fruitName2
    out += "."
    out += " He went out to get more and " + verb2
    out += " into a cardinal named " + birdname1
    out += ". She had seen " + catName1
    out += " and " + duckName
    out += " making the salad and wanted some, she offered him a " + fruitName2
    out += " in exchange for some of it when the salad was made. The cat agreed and returned to the house with the cardinal. When the salad was done she took her fill and flew off."
    out += " The duck and the cat stayed, eating and talking till " + Time1


    return out
