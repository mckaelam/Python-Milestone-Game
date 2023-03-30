import time
import textwrap
import random

RatCount = 0
Money = 0
Snacks = ''
Trenchcoat = False
Intro = "This is a story of a rat. Now, this is no ordinary rat, this is about a rat with a dream. An important one too.  So important, in fact, that he usually goes by: Steve O'Malley, Lord of Steveniros, and Ultimate Champions of all things Steve.\n\nBut you can just call him Steve.\n\nThe tragic reality of being a rat is that there are many things that they cannot do. This will not stop Steve from achieving his ultimate dream.\n\nTo go watch a movie in a movie theatre.\n\nNow, Steve could just sneak in, but that would ruin the experience. To fully experience this incredible event, he'll need to disguise himself as a human.\n\nYour job is to lead him through the sewers to the movie theatre while collecting everything he'll need to fully experience a movie."
Instructions = "You're going to need a couple of things to get into the movie theatre.\n\nFirst, you'll needs a trench coat! Everyone know that for a rat to impersonate a human, it needs a trench coat to pull it off.\n\nSecond, you'll need some rat friends to help fill out the trench coat. Maybe about 30 of them?\n\nThird, you need to buy a movie ticket once you get to the movie theatre. About $13 will do.\n\nLastly, don't forget a snack! No movie is complete without one.\n\n"
StartPoint = "Starting off on this epic journey, Steve doesn't know where to start and he could use some help. Where do YOU want to go first?"
AsciiRat = "                        ____    .-.\n                     .-\"`    `\",( __\_\n      .-==:;-._    .'         .-.     `'.\n    .'      `\"-:'-/          (  \} -=a  .)    <--- This is Steve.\n   /            \/       \,== `-  __..-'`\n'-'              |       |   |  .'\ `;\n                  \    _/---'\ (   `\"`\n                 /.`._ )      \ `;\n                 \`-/.'        `\"`\n                  `\"\`-.\n                     `\"`"
InvRat = " _  _\n(o)(o)--.\n \../ (  )    You're inventory is empty.\n m\/m--m\'`--."
AsciiCity = "                                    +              \n                                   / \\\n _____        _____     __________/ o \/\_________      _________\n|o o o|_______|    |___|               | | # # #  |____|o o o o  | /\\\n|o o o|  * * *|: ::|. .|               |o| # # #  |. . |o o o o  |//\\\\\n|o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  |((|))\n|o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  |((|))\n|_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|  |\n"
AsciiSewer = " .   .            .   .           .   .\n( ).( )          ( ).( )         ( ).( )\n (o o) .-._.\"     (o o) .-._.\"    (o o) .-._.\"\n(  -  )          (  -  )         (  -  )\n mm mm            mm mm           mm mm"
AsciiBreak = "        _\n       (( )_,     ,\n.--.    \ '/     /.\\\n    )   / \=    /O o\     _\n   (   / _/    /' o O| ,_( ))___     (`\n    `-|   )_  /o_O_'_(  \\'    _ `\    ) \n      `\"\"\"\"`            =`---<___/---'\n                            \"`"
Line = "__________________________________________________________________________________"

#functions to print different colors
def PrintRed(text):
    print("\033[91m {}\033[00m" .format(text))
def PrintGreen(text):
    print("\033[92m {}\033[00m" .format(text))
def PrintYellow(text):
    print("\033[93m {}\033[00m" .format(text))

def Wait():
    '''user interaction (press enter) to create a pause in dialogue'''
    PrEnter = "Press Enter to continue..."
    PrintGreen(PrEnter)
    input()

def InvWait():
    '''user interaction (press enter) to create a pause in dialogue'''
    PrEnter = "\nPress Enter to exit inventory..."
    PrintRed(PrEnter)
    input()

def PrintDelay(text):
    '''function that creates a delay in the output and also textwraps.
    Treat like a print() function'''
    Lines = text.split('\n')
    #separate lines by newline
    for rLine in Lines:
        #for text wrapping
        WrapText = textwrap.fill(rLine, width=80)
        #loop through charaters
        for i, char in enumerate(WrapText):
            print(char, end='', flush=True)
            time.sleep(0.05)
        #to handle \n
        print()
        time.sleep(0.05)

def CheckInv():
    '''function used to check what the user has collected'''
    #if there's nothing in the inventory
    if not RatCount and not Money and not Trenchcoat and not Snacks:
        print(Line)
        print(InvRat)
        InvWait()
    else:
        Rats = f"| Rats Obtained: {RatCount}            |"
        StMoney = f"| Money Obtained: ${Money}          |"
        StSnack = f"| Snack Obtained: {Snacks}"

        print("\n +------------------------------+\n | Inventory:                   |\n |                              |")
        if 1 <= RatCount <= 15:
            PrintRed(Rats)
        elif 16 <= RatCount <= 29:
            PrintYellow(Rats)
        elif RatCount > 30:
            PrintGreen(Rats)
        if 1 <= Money <= 7:
            PrintRed(StMoney)
        elif 8 <= Money <= 12:
            PrintYellow(StMoney)
        elif Money >= 13:
            PrintGreen(StMoney)
        if Trenchcoat is True:
            PrintGreen("| Trenchcoat Obtained: 1       |")
        if Snacks != '':
            PrintGreen(StSnack)
        print(" +------------------------------+")
        InvWait()

def GoMovie():
    if RatCount < 30 or Money < 13 or Trenchcoat is False or Snacks == '':
        PrintDelay("Steve went to the movies even though he wasn't completely ready. He likes to live life on the edge.\n")
    if RatCount >=30 and Money >= 13 and Trenchcoat is True and Snacks != '':
        if Snacks != '':
            PrintDelay("Steve heads on over to the movies, knowing with surity that he has everything he could possibly need for this movie.\n")
        if Snacks == '':
            PrintDelay("Steve heads on over to the movies, knowing with surity that he has everything he could possibly need for this movie.\n\nWell... probably.\n")
    if Trenchcoat is False:
        PrintDelay("To bad for him, though, because Steve doesn't even have a trenchcoat for all of his rat friends to fit into. There's no way they'll be able to impersonate a human.\n")
        if RatCount < 30:
            PrintDelay("Well, that would be a problem if Steve even had enough rat buddies. \n\nWhich he doesn't.\n\nMaybe if Steve had actually tried, he wouldn't be this dissapointed.\n")
        else:
            PrintDelay("He looks at all the rats that trusted his to lead them on this journey.\n\nHe had failed them.\n\nThe guilt of this moment would never leave Steve.\n\nHe was an absolute failure.\n")
    else:
        PrintDelay("While he has dragged the trenchcoat through the city, it has gotten quite dirty, but that's fine. No rat would care about a little dirt.\n")
        if RatCount < 30:
            PrintDelay("It's also not a problem, because there arent even enough rats to fill out the trenchcoat.\n\n In a single moment, all Steve's hopes and dreams are crushed.\n\n")
        else:
            PrintDelay("Steve directs the rats into the trenchcoat one by one. Once they're all inside, it's a little lumpy, and their 'human face' leave a lot to be desired, but it'll work.\n")
    if Money < 13:
        PrintDelay(f"Then he counts out the money he had collected along the way.\n\nHe comes up short with only ${Money}. The horror washes over him.\n\n All this hard work for nothing...\n")
    else:
        PrintDelay(f"Steve counts the money he has, and luckily he has enough, at ${Money}. He breathes out a sigh of relief.\n")
    if RatCount < 30 or Money < 13 or Trenchcoat is False:
        PrintDelay("With things the way they are, there's only one thing to do.\n\nSteve ditches any of the rats he gathered and sneaks into the movie theatre through the back to at least get a taste of the full movie experience. He crawls as quietly as possible and makes it inside.\n\nIt only takes a moment for someone to notice and they start screaming.\n\nSteve is chased outside, and he'll never recover from this horrible day...\n")
        PrintRed("\nYou failed. Press enter to exit the game...")
        input()
        exit()
    else:
        PrintDelay("The bumpy, unsightly mass of rats in a trenchcoat walk up to the ticket booth. Luckily for Steve the employee doesn't even question it.\n\nThey've seen weirder.\n")
        PrintDelay("While Steve doesn't speak human, he's a great pantomime.\n\nControlling the rat mass he pantomimes what movie he wants to watch and hands the employee the money for the ticket. Through some miracle everything goes great, and Steve now has a ticket to Sharknado 23.\n")
        PrintDelay("The rat mass enters the movie and takes a seat.\n\nSteve has never been more ecstatic in his life.\n")
        if Snacks == '':
            PrintDelay("As the movie starts, Steve realizes in horror that he forgot a snack. All this hard work, and to get this far...\n\nAll for nothing.\n\nFor the rest of the movie, Steve can't even see anything through the tears in his eyes...")
            PrintRed("\nYou failed. Press enter to exit the game...")
            input()
            exit()
        if Snacks != 'cheese':
            PrintDelay(f"As the movie starts, Steve takes out the {Snacks}. Steve enjoys the absolute masterpiece that it Sharknado 23, but he kinda wishes he had gotten a better snack...")
            PrintRed("\nYou failed. Press enter to exit the game...")
            input()
            exit()
        else:
            PrintDelay("As the movie starts, Steve smuggly takes out the cheese he had found previously. An amazing snack with an amazing movie. Nothing could possible beat this moment.\n")
            PrintGreen("\nYou did it! Press enter to exit the game...")
            input()
            exit()

"""
                            HERE'S ALL THE FUNCTIONS
*************************** FOR THE GAMES TO PLAY TO ***************************
                            GAIN MORE RAT BUDDIES
"""

def CupGame():
    PrintDelay('''Steve comes up on a group of rats. They seem to be playing some kind of game.\n\nAs he gets closer he sees that they're playing the shell game.\n\nOne rat moves the three cups around at lightning speed. So quickly, in fact, that Steve can't keep up, but maybe you can impress these rats by guessing right and they'll join you on your quest to go to the movie theatre.''')
    PrintYellow("\nWhich cup do you think has the ball underneath it?")
    print("\n   .---.     .---.     .---.\n  /=====\   /=====\   /=====\\\n ‘-------’ ‘-------’ ‘-------’\n")
    while True:
        Answer = random.randint(1, 3)
        IntGuess = input("Choose 1, 2, or 3: ")
        try:
            InputGuess = int(IntGuess)
            if InputGuess < 1 or InputGuess > 3:
                PrintRed("\nInvalid input. Please input a valid number.\n")
            else:
                break
        except ValueError:
            PrintRed("\nInvalid input. Please input a number.\n")
    print(Line)
    if Answer == 1:  
            print("\n     _       .---.     .---.\n    (_)     /=====\   /=====\\\n           ‘-------’ ‘-------’")
    elif Answer == 2:
            print("\n   .---.       _        .---.\n  /=====\     (_)      /=====\\\n ‘-------’            ‘-------’")
    else:
            print("\n   .---.     .---.        _\n  /=====\   /=====\      (_)\n ‘-------’ ‘-------’ ")

    if Answer == InputGuess:
        AddRat = random.randint(8, 10)
        global RatCount
        RatCount += AddRat
        PrintDelay(f'''\n\nYou guessed right! The rats around you cheer for your success and are indeed very impressed.\n\n{AddRat} rats decided to join you on your journey.''')
        print(Line)
    else:
        PrintDelay(f'''\nOh darn, looks like you got the answer wrong... The rats around you scurry off into the distance.''')
        print (Line)

def GuessGame():
    PrintDelay("Steve scurries down further into the sewers trying to find more rats. After a couple different turns he comes across another group of rats.\n\nSteve explain what he's trying to do in hopes that they'll get just excited as he is about watching a movie. They look a little sceptical, but one says that they'll join if Steve win a game against them\n")
    PrintYellow("I'm thinking of a number between 1 and 10.\" the rat crows.\n\n")
    Answer = random.randint(1, 10)

    while True:
        Guess = input("Guess the number: ")
        try:
            GuessNum = int(Guess)
            if GuessNum < 1 or GuessNum > 10:
                PrintRed("\nInvalid input. Please input a number between 1 and 10.\n")
            elif GuessNum < Answer:
                PrintDelay("\n\"Hmm. Nope, your guess is too low. Try again.\", the boss rat tells you.\n")
            elif GuessNum > Answer:
                PrintDelay("\n\"Hmm. Nope, your guess is too high. Try again.\", the boss rat tells you.\n")
            if GuessNum == Answer:
                AddRat = random.randint(8, 10)
                global RatCount
                RatCount += AddRat
                PrintDelay(f'''\nSteve guessed right! The rats around him cheer.\n\n{AddRat} rats join you on your journey to the movies.\n''')
                print(Line)
                break
        except ValueError:
            PrintRed("\nInput error. Please input a number.\n")
            continue
 
TryAgain = "\"That's the spirit!\"\n\n"
NewRiddle = '''\"That's the spirit! I have so many riddles, I'm pretty sure I'll never run out.\n\n Here's another one\"\n\n'''
GiveUp = '''\nThe random rat looks a little sad, but he understands. Riddles can be hard to figure out. They're not angry, just disappointed. The rat scurries off back into the sewers.\n'''
def RiddleCorrect():
    AddRat = random.randint(5, 10)
    global RatCount
    RatCount += AddRat
    PrintDelay(f'''\n\"Amazing! You got the answer right!\" the random rat says.\n\nOh, I didn't even say how many rat buddies were going to join you... Worry not, {AddRat} rats are joining you on your adventure!\"\n''')
    PrintDelay("\"I have soooooo many more riddles though. Do you want to answer another one? I'm sure I can scrounge up some more rat buddies if you answer right again!\"\n\nDo you want to answer more riddles to get more rat buddies or try and find more on your own?\n")
    
    while True:
        StopCont = int(input("1. Leave\n2. Try another riddle\n\nYour choice: "))
        if StopCont == 1:
            PrintDelay(GiveUp)
            break
        elif StopCont == 2:
            PrintDelay(NewRiddle)
            break
        else:
            print("\nInput Error. Try again\n")

Riddles = {
    1: {
        'text': "What has a head and a tail but no body?",
        'answer': "coin",
        'hint': "\nYou'll need to collect some of this if you want a movie ticket...\n",
    },
    2: {
        'text': "What starts with an E, ends with an E, but only contains one letter?",
        'answer': "envelope",
        'hint': "Humans send texts nowadays...\n",
    },
    3: {
        'text': "What has four legs in the morning, two legs in the afternoon, and three legs in the evening?",
        'answer': "human",
        'hint': "\nSteve will be trying to impersonate one of these later...\n",
    },
    4: {
        'text': "What runs but never walks, has a mouth but never talks, has a bed but never sleeps, has a head but never weeps?",
        'answer': "river",
        'hint': "\nRats are actually great swimmers! Maybe not in moving water though...\n",
    },
    5: {
        'text': "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        'answer': "fire",
        'hint': "\nBest not to get to close to these or they'll burn you...\n",
    },
    6: {
        'text': "The more you look at it, the less you see. What is it?",
        'answer': "darkness",
        'hint': "\nSteve can't see in the sewers sometimes because of how dark it is. Especially at night...\n",
    },
}
def Riddle():
    AnsHint = "\nType out your guess or ask for a hint by typing 'hint'\n\n------------> "
    WrongAsn = "\nNope, that wasn't the answer the rat was looking for... Do you want to give up? Or try again?\n"
    GiveTry = "1. Give up\n2. Try another riddle\n\nYour choice: "

    PrintDelay('''As Steve continues on down the sewers, he's sees another rat scramble their way towards him.\n\n\"Hey! I heard you were looking to get a group of rats together! Me and my buddies are willing to join me if you can answer a riddle.\n\nSteve is always up for a challenge and agrees. \n\n\"Great! Here's a riddle for you:\"\n''')
    RiddleCount = 1
    MoreRiddle = True
    while MoreRiddle is True:
        RiddleDone = False
        riddle = Riddles[RiddleCount]

        PrintYellow(riddle['text'])
        while RiddleDone is False:
            guess = input(AnsHint).lower()
            if guess == riddle['answer']:
                RiddleCount +=1
                AddRat = random.randint(8, 10)
                global RatCount
                RatCount += AddRat
                PrintDelay(f'''\n\"Amazing! You got the answer right!\" the random rat says.\n\nOh, I didn't even say how many rat buddies were going to join you... Worry not, {AddRat} rats are joining you on your adventure!\"\n''')
                PrintDelay("\"I have soooooo many more riddles though. Do you want to answer another one? I'm sure I can scrounge up some more rat buddies if you answer right again!\"\n\n")
                UserContinue = input("1. Leave\n2. Try another riddle\n\nYour choice: ")
                if UserContinue == '1':
                    #change print maybe...
                    PrintDelay(GiveUp)
                    MoreRiddle = False
                    RiddleDone = True
                if UserContinue == '2':
                    RiddleDone = True
            elif guess == 'hint':
                print("\n")
                PrintDelay(riddle['hint'])
                PrintYellow(riddle['text'])
            else:
                PrintDelay(WrongAsn)
                UserContinue = input(GiveTry)
                if UserContinue == '1':
                    PrintDelay(GiveUp)
                    print(Line)
                    MoreRiddle = False
                    RiddleDone = True
                elif UserContinue == '2':
                    PrintDelay("\nThe random rat is more than happy to give you another riddle.\n")
                    RiddleDone = True
                else:
                    print("\nInput Error. Try again\n")
            if RiddleCount == 7:
                PrintDelay("\"Oh wow, you answer all the riddles I had!\"\n\nThe rat scurries back into the sewer...")
                MoreRiddle = False
                RiddleDone = True

def RockPaperScissors():
    PrintDelay("\nSteve finds a rat that wants to play rock paper scissors with you. Maybe if you win, they'll help you find some rats for your adventure!")
    PrintYellow("\n+--------------+\n| 1. Rock      |\n| 2. Paper     |\n| 3. Scissors  |\n+--------------+\n\n")
    while True:
        User = input("Your Choice: ")
        try:
            UserNum = int(User)
            if UserNum < 1 or UserNum > 3:
                PrintRed("Invalid input. Please input a number between 1 and 3.")
            else:
                break
        except ValueError:
            PrintRed("Invalid input. Please enter a valid integer.")
    while True:
        Computer = random.randint(1,3)
        if UserNum == Computer:
            PrintDelay("It's a tie! Try again.")
        elif (UserNum == 1 and Computer == 3) or (UserNum == 3 and Computer == 2) or (UserNum == 2 and Computer == 1):
            PrintDelay("You won!")
            AddRat = random.randint(8, 10)
            global RatCount
            RatCount += AddRat
            PrintDelay(f"\n{AddRat} rats have joined you on your journey.")
            break
        else:
            PrintDelay("You lost! Try again.")
            while True:
                User = input("Your Choice: ")
                try:
                    UserNum = int(User)
                    if UserNum < 1 or UserNum > 3:
                        PrintRed("Invalid input. Please input a number between 1 and 3.")
                    else:
                        break
                except ValueError:
                    PrintRed("Invalid input. Please enter a valid integer.")

"""
                               HERE'S THE FUNCTION
*************************** FOR STEVE TO GATHER MONEY, ***************************
                           SNACKS, AND COAT IN THE CITY
"""
SnackYN = "+-------+\n|1. Yes  |\n|2. No   |\n+--------+\n"
BadPick = "\nWell, who knows if we'll find a different snack. Might as well take this one..."
DontPick = "Surely there's a better snack out there! Steve will keep looking.\n\n"

def BadSnack(snack):
    global Snacks
    PrintDelay(f"Steve found a(n) {snack}. That would work as a snack, but it's not the best...\n\nDo you want to take it anyways?\n")
    PrintYellow(SnackYN)
    while True: 
        try:
            SnackChoice = int(input("Your Choice: "))
        except ValueError:
            PrintRed("Invalid input. Please enter a number.")
        if SnackChoice == 1:
            Snacks = snack
            PrintDelay(BadPick)
            break
        elif SnackChoice == 2:
            PrintDelay(DontPick)
            break
        else:
            PrintRed("Invalid input. Please enter a valid number.")

def CityChoice():
    global Money
    global Trenchcoat
    global Snacks
    AppleOption = False
    TunaOption = False
    SandwichOption = False
    CheeseOption = False
    
    PrintDelay("\nSteve agrees that he should go to the city. He could find a snack or maybe even a trench coat there.\n")
    print(AsciiCity)
    print(Line)
    Wait()

    while True:
        PrintDelay("\nWhere would you like to go?\n")
        PrintYellow("+---------------------------+\n| 1. Turn left               |\n| 2. Turn right              |\n| 3. Go to the movie theatre |\n| 4. Check inventory         |\n| 5. Leave                   |\n+----------------------------+\n")
        User = input("Your Choice: ")
        print("\n")
        if User == '3':
            GoMovie()
            break
        elif User == '4':
            CheckInv()
        elif User == '5':
            PrintDelay("\nSteve decides he's done exploring the city...")
            print(Line)
            print("\n")
            break
        elif User == '1' or User == '2':
            Chance = random.randint(1, 100)
            if User == '1':
                if 1 >= Chance <= 50:
                    MoneyGain = random.randint(1, 2)
                    Money += MoneyGain
                    PrintDelay("Steve runs down a road looking around, and sees some change on the ground. What luck!\n")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 51 >= Chance <= 63:
                    PrintDelay("As Steve looks around, he sees something under a bush...\n")
                    if Trenchcoat == False:
                        Trenchcoat = True
                        PrintDelay("Steve found a trench coat! It'll be hard to carry, but Steve never skips leg day!")
                        PrintDelay("\nA trenchcoat has been added to your inventory.")
                    else:
                        MoneyGain = random.randint(1, 3)
                        Money += MoneyGain
                        PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 64 >= Chance <= 76:
                    MoneyGain = random.randint(3, 4)
                    Money += MoneyGain
                    PrintDelay(f"There's a small park the Steve sees as he turns. He searches around for a while and finds ${MoneyGain}. Steve wonders if taking this is ethical...\n\nWell, Steve's a rat, so he doesn't care about ethics!\n")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 77 >= Chance <= 89:
                    PrintDelay("look underneath a newspaper")
                    MoneyGain = random.randint(2, 4)
                    Money += MoneyGain
                    PrintDelay(f"Steve sees a dumpster! Surely there's something good in there! Steve scurries his way into the trash.\n\n")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 90 >= Chance <= 96:
                    MoneyGain = random.randint(5, 7)
                    Money += MoneyGain
                    PrintDelay(f"Steve continues his journey through New York City and comes up on a water fountain. He looks in the water an see's money change at the bottom.\n\n")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
                else:
                    PrintDelay("look as a human drops money.")
                    MoneyGain = random.randint(10, 12)
                    Money += MoneyGain
                    PrintDelay(f"As Steve turns the corner of a building, he sees a human drop their wallet. What a great day this is! Steve, because he's a rat without any ethics, doesn't feel bad at all when he takes ${MoneyGain} from it.")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
            elif User == '2':
                if Chance < 51:
                    if Snacks == '' and AppleOption == False:
                        AppleOption = True
                        BadSnackChoice = 'apple'
                        BadSnack(BadSnackChoice)
                    else:
                        MoneyGain = random.randint(1, 2)
                        Money += MoneyGain
                        PrintDelay(f"Steve runs down an alleyway. It's quite messy down there, but ask he searches around, he found ${MoneyGain}!\n")
                        PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 51 >= Chance <= 63:
                    if Snacks == '' and TunaOption == False:
                        TunaOption = True
                        BadSnackChoice = 'half a can of tuna'
                        BadSnack(BadSnackChoice)
                    else:
                        MoneyGain = random.randint(1, 3)
                        Money += MoneyGain
                        PrintDelay(f"Steve runs up to a bench. He checks around and finds ${MoneyGain} underneath it. How lucky!\n")
                        PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 64 >= Chance <= 76:
                    #gutter
                    if Snacks != '' or CheeseOption == True:
                        MoneyGain = random.randint(1, 2)
                        Money += MoneyGain
                        PrintDelay(f"Steve find a tree surrounded by trash. As he digs inside he find some money!\n")
                        PrintDelay(f"${MoneyGain} has been added to you inventory")
                    else:
                        SnackOption = 'cheese'
                        CheeseOption = True
                        PrintDelay("Steve found a nice chunk of cheese. What a great snack this would be! \n\nDo you want to take it?\n")
                        PrintYellow(SnackYN)
                        while True:
                            try:
                                SnackChoice = int(input("Your Choice: "))
                            except ValueError:
                                PrintRed("Invalid input. Please enter a number.")
                            if SnackChoice == 1:
                                Snacks = SnackOption
                                PrintDelay("\nGreat! Steve takes the cheese and stores it away for the movie.\n\nCheese has been added to your inventory.")
                                break
                            elif SnackChoice == 2:
                                PrintDelay("\nWell... Maybe there's another snack you could find that's better... but probably not.\n\n")
                                break
                            else:
                                PrintRed("Invalid input. Please enter a valid number.")
                elif 77 >= Chance <= 89:
                    if Snacks == '' and SandwichOption == False:
                        SandwichOption = True
                        BadSnackChoice = 'partially eaten sandwich'
                        BadSnack(BadSnackChoice)
                    else:
                        MoneyGain = random.randint(2, 4)
                        Money += MoneyGain
                        PrintDelay(f"There's a newspaper on the ground. As Steve inspects it, ${MoneyGain} fell from it.\n")
                        PrintDelay(f"${MoneyGain} has been added to you inventory")
                elif 90 >= Chance <= 96:
                    MoneyGain = random.randint(5, 7)
                    Money += MoneyGain
                    PrintDelay(f"Steve moves through the city and wanders up into someone's balcony. He finds ${MoneyGain} caught in the sliding door.\n")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
                else:
                    MoneyGain = random.randint(10, 12)
                    Money += MoneyGain
                    PrintDelay(f"Steve crawls around, and somehow ends up in a gutter. While wandering around he sees some cash on")
                    PrintDelay(f"${MoneyGain} has been added to you inventory")
        else:
            PrintRed("\nInvalid input. Please input Left(1), Right(2), or Leave(3)\n")    

"""                           

*************************** LAST CHOICE FUNCTIONS ***************************
                            
"""

def SewerChoice():
    global RatCount
    LeaveSewer = False
    while LeaveSewer is False:
        Continue = False
        PrintDelay("Steve agrees that he should go to the sewers. He could find some rat buddies there.\n\nHe scurries down...\n")
        print(AsciiSewer)
        print(Line)
        Wait()
        CupGame()
        LeaveSewer = False
        Continue = False
        while Continue is False:
            PrintYellow("+------------------------+\n| 1. Continue             |\n| 2. Check Inventory      |\n| 3. Leave                |\n+-------------------------+\n")
            User = input("Your Choice: ")
            print("\n")
            if User == '1':
                PrintDelay("Steve continues down the sewer...\n")
                print(AsciiBreak)
                print(Line)
                Wait()
                Continue = True
            elif User == '2':
                CheckInv()
            elif User == '3':
                PrintDelay("\nSteve decided to leave the sewer...\n")
                LeaveSewer = True
                Continue = True
                return
        GuessGame()
        LeaveSewer = False
        Continue = False
        while Continue is False:
            PrintYellow("+---------------------------+\n| 1. Continue                |\n| 2. Check Inventory         |\n| 3. Leave                   |\n+----------------------------+\n")
            User = input("Your Choice: ")
            print("\n")
            if User == '1':
                PrintDelay("\nSteve continues down the sewer...\n")
                print(AsciiBreak)
                print(Line)
                Wait()
                Continue = True
            elif User == '2':
                CheckInv()
            elif User == '3':
                PrintDelay("\nSteve decided to leave the sewer...\n")
                LeaveSewer = True
                Continue = True
                return
        PrintDelay("A rat crawls out from the shadows of the sewer.\n\n\"Hey, you. Yeah, you. I heard you were trying to get into the movies.\"\n\n\"If you turn left enough in the city, you'll find a trenchcoat. Don't ask me how I know...\"\n\nThe rat joins you on your journey.\n")
        RatCount += 1
        LeaveSewer = False
        Continue = False
        while Continue is False:
            PrintYellow("+---------------------------+\n| 1. Continue                |\n| 2. Check Inventory         |\n| 3. Leave                   |\n+----------------------------+\n")
            User = input("Your Choice: ")
            print("\n")
            if User == '1':
                PrintDelay("\nSteve continues down the sewer...\n")
                print(AsciiBreak)
                print(Line)
                Wait()
                Continue = True
            elif User == '2':
                CheckInv()
            elif User == '3':
                PrintDelay("\nSteve decided to leave the sewer...\n")
                LeaveSewer = True
                Continue = True
                return
        Riddle()
        LeaveSewer = False
        Continue = False
        while Continue is False:
            PrintYellow("+---------------------------+\n| 1. Continue                |\n| 2. Check Inventory         |\n| 3. Leave                   |\n+----------------------------+\n")
            User = input("Your Choice: ")
            print("\n")
            if User == '1':
                PrintDelay("\nSteve continues down the sewer...\n")
                print(AsciiBreak)
                print(Line)
                Wait()
                Continue = True
            elif User == '2':
                CheckInv()
            elif User == '3':
                PrintDelay("\nSteve decided to leave the sewer...\n")
                LeaveSewer = True
                Continue = True
                return
        PrintDelay("A rat crawls out from the shadows of the sewer.\n\n\"Hey, you. Yeah, you. I heard you were trying to get into the movies.\"\n\n\"If you turn right enough in the city, you'll find a snack. Don't ask me how I know...\"\n\nThe rat joins you on your journey.\n")
        RatCount += 1
        LeaveSewer = False
        Continue = False
        while Continue is False:
            PrintYellow("+---------------------------+\n| 1. Continue                |\n| 2. Check Inventory         |\n| 3. Leave                   |\n+----------------------------+\n")
            User = input("Your Choice: ")
            print("\n")
            if User == '1':
                PrintDelay("\nSteve continues down the sewer...\n")
                print(AsciiBreak)
                print(Line)
                Wait()
                Continue = True
            elif User == '2':
                CheckInv()
            elif User == '3':
                PrintDelay("\nSteve decided to leave the sewer...\n")
                LeaveSewer = True
                Continue = True
                return
        RockPaperScissors()
        LeaveSewer = False
        Continue = False
        while Continue is False:
            PrintYellow("+---------------------------+\n| 1. Continue                |\n| 2. Check Inventory         |\n| 3. Leave                   |\n+----------------------------+\n")
            User = input("Your Choice: ")
            print("\n")
            if User == '1':
                PrintDelay("\nSteve continues down the sewer...\n")
                print(AsciiBreak)
                print(Line)
                Wait()
                Continue = True
            elif User == '2':
                CheckInv()
            elif User == '3':
                PrintDelay("\nSteve decided to leave the sewer...\n")
                LeaveSewer = True
                Continue = True
                return
