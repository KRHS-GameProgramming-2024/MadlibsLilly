from Getters import *

def Story2(debug = False):

    if debug: print ("Story2 Function")
    print ("\n")
    Name1 = getWord("Enter a name: ", debug)
    print ("\n")
    Place1 = getWord ("Enter a place: ", debug)
    print ("\n")
    Name2 = getWord("Enter a name: ", debug)
    print ("\n")
    Verb1 = getWord("Enter a verb: ", debug)
    print ("\n")
    Chip = getChip("Enter a kind of chip: ", debug)
    print ("\n")
    Noun1 = getWord ("Enter a noun: ", debug)
    print ("\n")
    Verb2 = getWord ("Enter a verb: ", debug)
    print ("\n")
    saidSaid = getSaidMenu  ("Pick one from the list: ", debug)

    out = ""
    out += "    " + Name1
    out += " didn't want to go to " + Place1
    out += " the next day. So she told her father that she wouldn't go, he laughed and said she had to anyway." + Name1
    out += " then went to find her mother and told her the same thing, her mother also told her she had to go."
    out += "So she took matters into her own hands, they couldn't send her to " + Place1
    out += " if she was sick. She woke up the next morning and told her parents she didn't feel good"
    out += " but when they checked her tempurature it was normal so off to " + Place1
    out += " she went."
    out += " At lunch she was talking to her friend " + Name2
    out += " About her plan, he " + Verb1
    out += " at her, crunching his " + Chip
    out += " He told her to wait a few days so they didn't suspect and put something warm on her face before coming up to them and she'd stay home for sure."
    out += " Armed with her new plan, " + Name1
    out += " bided her time, when three days had passed, she put a warm " + Noun1
    out += " across her face until her skin was warm and went into her parents room."
    out += " 'Mom, Dad, I don't feel good,' she said, resisting the urge to " + Verb2
    out += " as her father laid his hand across her forehead."
    out += " 'you have a fever kiddo,' He " + saidSaid
    out += ", 'go get some rest'"
    out += " " + Name1
    out += " beamed internally, 'so I don't have to go to " + Place1
    out += " ?'"
    out += " Her mother laughed, 'sweetheart it's saturday!'"

    return out
