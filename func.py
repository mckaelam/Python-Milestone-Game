import time
import textwrap
import random

NumRats = 0
Money = 0
Snacks = ''
Trenchcoat = False
MovieTicket = False
Intro = "This is a story of a rat. Now, this is no ordinary rat, this is about a rat with a dream. An important one too.  So important, in fact, that he usually goes by: Steve O'Malley, Lord of Steveniros, and Ultimate Champions of all things Steve.\n\nBut you can just call him Steve.\n\nThe tragic reality of being a rat is that there are many things that they cannot do. This will not stop Steve from achieving his ultimate dream.\n\nTo go watch a movie in a movie theatre.\n\nNow, Steve could just sneak in, but that would ruin the experience. To fully experience this incredible event, he'll need to disguise himself as a human.\n\nYour job is to lead him through the sewers to the movie theatre while collecting everything he'll need to fully experience a movie."
Instructions = "You're going to need a couple of things to get into the movie theatre.\n\nFirst, you'll needs a trench coat! Everyone know that for a rat to impersonate a human, it needs a trench coat to pull it off.\n\nSecond, you'll need some rat friends to help fill out the trench coat. Maybe about 54 of them?\n\nThird, you need to buy a movie ticket once you get to the movie theatre. About $13 will do.\n\nLastly, don't forget a snack! No movie is complete without one.\n\n"
StartPoint = "Starting off on this epic journey, Steve doesn't know where to start and he could use some help. Where do YOU want to go first?"
AsciiRat = "                        ____    .-.\n                     .-\"`    `\",( __\_\n      .-==:;-._    .'         .-.     `'.\n    .'      `\"-:'-/          (  \} -=a  .)\n   /            \/       \,== `-  __..-'`\n'-'              |       |   |  .'\ `;\n                  \    _/---'\ (   `\"`\n                 /.`._ )      \ `;\n                 \`-/.'        `\"`\n                  `\"\`-.\n                     `\"`"
InvRat = " _  _\n(o)(o)--.\n \../ (  )    You're inventory is empty.\n m\/m--m\'`--."
Line = "__________________________________________________________________________________"

#functions to print different colors
def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): 
    print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): 
    print("\033[93m {}\033[00m" .format(skk))

#user interaction (press enter) to create a pause in dialogue
def Wait():
    PrEnter = "Press Enter to continue..."
    prGreen(PrEnter)
    input()

def InvWait():
    PrEnter = "Press Enter to exit inventory..."
    prRed(PrEnter)
    input()

#function that creates a delay in the output
def printDelay(text):
    lines = text.split('\n')
    for line in lines:
        WrapText = textwrap.fill(line, width=80)
        for i, char in enumerate(WrapText):
            if i > 0 and WrapText[i-1] != ' ':
                time.sleep(0.005)
            print(char, end='', flush=True)
            time.sleep(0.001)
        print()
        time.sleep(0.1)


def Choises(*options):
    fixed_options = ['check inventory', 'go to the movie now']
    variable_options = list(options)
    all_options = fixed_options + variable_options
    for i, option in enumerate(all_options):
        #maybe change this to all options
        if i < len(fixed_options):
            # fixed options have a box around them
            print(f"{i+1}. |{'_'*(len(option)+2)}|")
            print(f"   | {option} |")
            print(f"   |{'-'*(len(option)+2)}|")
        else:
            print(f"{i+1}. {option}")
    while True:
        #user input needed
        choice = input("Enter the number of your choice: ")
        #error handling
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        #turn into int
        choice = int(choice)
        #more error handling
        if choice < 1 or choice > len(all_options):
            print(f"Invalid choice. Please enter a number between 1 and {len(all_options)}.")
            continue
        if choice == 1:
            CheckInv()
        elif choice == 2:
            GoMovie()
        else:
            func = variable_options[choice-3]
            func()
            return

#function used to check what the user has collected
def CheckInv():
    #if there's nothing in the inventory
    if not NumRats and not Money and not Trenchcoat and not MovieTicket and not Snacks:
        print(Line)
        print(InvRat)
        InvWait()
        exit()
    
    Rats = f"Rats Obtained: {NumRats}\n"
    StMoney = f"Money Obtained: ${Money}\n"
    StSnack = f"Snack Obtained: {Snacks}"

    print("Inventory:\n\n")
    if 1 <= NumRats <= 29:
        prRed(Rats)
    elif 30 <= NumRats <= 53:
        prYellow(Rats)
    elif NumRats > 54:
        prGreen(Rats)
    if 1 <= Money <= 7:
        prRed(StMoney)
    elif 8 <= Money <= 13:
        prYellow(StMoney)
    elif Money >= 14:
        prGreen(StMoney)
    if Trenchcoat == True:
        prGreen("Trenchcoat Obtained: 1")
    if MovieTicket == True:
        prGreen("Movie Ticket Obtained: 1")
    if Snacks != '':
        prGreen(StSnack)

    InvWait()
    exit()

def GoMovie():
    print("Steve went to the movies")

"""
                            HERE'S ALL THE FUNCTIONS
*************************** FOR THE GAMES TO PLAY TO ***************************
                            GAIN MORE RAT BUDDIES
"""
def CupGame():
    printDelay('''Steve comes up on a group of rats. They seem to be playing some kind of game.\n\nAs he gets closer he sees that they're playing the shell game.\n\nOne rat moves the three cups around at lightning speed. So quickly, in fact, that Steve can't keep up, but  maybe you can impress these rats by guessing right and they'll join you on your quest to go  the movie theatre.''')
    ChooseWhich = '''\nWhich cup do you think has the ball underneath it?\n\n   .---.     
    .---.     .---.\n  /=====\   /=====\   /=====\\\n ‘-------’ ‘-------’ ‘-------’\n\nChoose 1, 2, or 3: '''
    Answer = random.randint(1, 3)
    InputGuess = int(input(ChooseWhich))
   
    print(Line)
    
    if Answer == 1:
        print("\n     _       .---.     .---.\n    (_)     /=====\   /=====\\\n           ‘-------’ ‘-------’")
    elif Answer ==2:
        print("\n   .---.       _        .---.\n  /=====\     (_)      /=====\\\n ‘-------’            ‘-------’")
    else:
        print("\n   .---.     .---.        _\n  /=====\   /=====\      (_)\n ‘-------’ ‘-------’ ")
    
    if Answer == InputGuess:
        AddRat = random.randint(5, 10)
        global NumRats
        NumRats += AddRat
        printDelay(f'''\n\nYou guessed right! The rats around you cheer for your success and are indeed very impressed.\n\n{AddRat} rats decided to join you on your journey.''')
    else:

        printDelay(f'''\n\nOh darn, looks like you got the answer wrong... The rats around you scurry off into the distnace.''')


def GuessGame():
    printDelay('''Steve scurries down further into the sewers trying to find more rats. After a couple different turns he comes ac ross another group of rats.\n\nSteve explain what he's trying to do in hopes that they'll get just excited as he is about watching a movie. They look a little sceptical, but one says that they'll join in you win a game against them\n\n\"I'm thinking of a number between 1 and 10.\" the rat crows. \n\n\"If you guess it right within 3 tries we'll join you\"\n\n''')
    Answer = random.randint(1, 10)
    GuessesLeft = 3

    while GuessesLeft > 0:
        try:
            Guess = int(input("Guess the number: "))
        except ValueError:
            print("Input error. Try again.")
            continue
        
        if Guess == Answer:
            AddRat = random.randint(5, 10)
            global NumRats
            NumRats += AddRat
            printDelay(f'''\nYou guess right! The rats around you cheer fo you.\n\n{AddRat} rats join you on your journey to the movies.''')
            break
        elif Guess < Answer:
            printDelay("\"Hmm. Nope, your guess is too low. Try again.\", the boss rat tells you.")
        else:
            printDelay("\"Hmm. Nope, your guess is too high. Try again.\", the boss rat tells you.")

    GuessesLeft -= 1

    if GuessesLeft == 0:
        printDelay(f'''\"Sorry, you ran out of guesses. The number I was thinking of was {Answer}. Better luck next time\" the boss rat tells you. The surrounding rats scurry  away.''')

TryAgain = "\"That's the spirit!\"\n\n"
NewRiddle = '''\"That's the spirit! I have so many riddles, I'm pretty sure I'll never run out.\n\n Here's another one\"\n\n'''
GiveUp = '''The random rat looks a little sad, but he understands. Riddles can be hard to figure out. They're not angry, just disappointed. The rat scurries off back into the sewers.'''
def RiddleCorrect():
    AddRat = random.randint(5, 10)
    global NumRats
    NumRats += AddRat
    printDelay(f'''\n\"Amazing! You got the answer right!\" the random rat says.\n\nOh, I didn't even say how many rat buddies were going to join you... Worry not, {AddRat} rats are joining you on your adventure!\"\n''')
    printDelay("\"I have soooooo many more riddles though. Do you want to answer another one? I'm sure I can scrounge up some more rat buddies if you answer right again!\"\n\nDo you want to answer more riddles to get more rat buddies or try and find more on your own?\n")
    
    while True:
        StopCont = int(input("1. Leave\n2. Try another riddle\n\nYour choice: "))
        if StopCont == 1:
            printDelay(GiveUp)
            break
        elif StopCont == 2:
            printDelay(NewRiddle)
            break
        else:
            print("\nInput Error. Try again\n")

riddles = {
    1: {
        'text': "What has a head and a tail but no body?",
        'answer': "coin",
        'hint': "You'll need to collect some of this if you want a movie ticket...",
    },
    2: {
        'text': "What starts with an E, ends with an E, but only contains one letter?",
        'answer': "envelope",
        'hint': "Humans send texts nowadays...",
    },
    3: {
        'text': "What has four legs in the morning, two legs in the afternoon, and three legs in the evening?",
        'answer': "human",
        'hint': "Steve will be trying to impersonate one of these later...",
    },
    4: {
        'text': "What runs but never walks, has a mouth but never talks, has a bed but never sleeps, has a head but never weeps?",
        'answer': "river",
        'hint': "Rats are actually great swimmers! Maybe not in moving water though...",
    },
    5: {
        'text': "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        'answer': "fire",
        'hint': "Best to stay away when you see one. It's burned Steve's fur a couple of times...",
    },
    6: {
        'text': "The more you look at it, the less you see. What is it?",
        'answer': "darkness",
        'hint': "Steve can't see sometimes in the sewers. Especially at night...",
    },
}
def Riddle():
    AnsHint = "\n\nType out your guess or ask for a hint by typing 'hint'\n\n------------> "
    WrongAsn = "\nNope, that wasn't the answer the rat was looking for... Do you want to give up? Or try again?\n"
    GiveTry = "1. Give up\n2. Try another riddle\n\nYour choice: "
 
    #printDelay('''As Steve continues on down the sewers, he's sees another rat scramble their way towards him.\n\n\"Hey! I heard you were looking to get a group of rats together! Me and my buddies are willing to join me if you can answer a riddle.\n\nSteve is always up for a challenge and agrees. \n\n\"Great! Here's a riddle for you:\"\n\n''')

    give_up = False
    while not give_up:
        riddle_choice = random.randint(1, 6)
        riddle = riddles[riddle_choice]

        prYellow(riddle['text'])
        guess = input(AnsHint).lower()

        if guess == riddle['answer']:
            AddRat = random.randint(5, 10)
            global NumRats
            NumRats += AddRat
            printDelay(f'''\n\"Amazing! You got the answer right!\" the random rat says.\n\nOh, I didn't even say how many rat buddies were going to join you... Worry not, {AddRat} rats are joining you on your adventure!\"\n''')
            printDelay("\"I have soooooo many more riddles though. Do you want to answer another one? I'm sure I can scrounge up some more rat buddies if you answer right again!\"\n\nDo you want to answer more riddles to get more rat buddies or try and find more on your own?\n")

            while True:
                StopCont = int(input("1. Leave\n2. Try another riddle\n\nYour choice: "))
                if StopCont == 1:
                    printDelay(GiveUp)
                    return
                elif StopCont == 2:
                    break
                else:
                    print("\nInput Error. Try again\n")

            continue

        elif guess == 'hint':
            printDelay(riddle['hint'])
            continue

        else:
            printDelay(WrongAsn)
            try:
                wrong_response = int(input(GiveTry))
            except ValueError:
                print("\nInput Error. Try again\n")
                continue

            if wrong_response == 1:
                printDelay(GiveUp)
                give_up = True
            elif wrong_response == 2:
                printDelay("\nThe random rat is more than happy to give you another riddle.\n")
                continue
            else:
                print("\nInput Error. Try again\n")
    # give_up = False
    # while not give_up:
    #     riddle_choice = random.randint(1, 6)
    #     riddle = riddles[riddle_choice]
        
    #     prYellow(riddle['text'])
    #     guess = input(AnsHint).lower()
        
    #     if guess == riddle['answer']:
    #         AddRat = random.randint(5, 10)
    #         global NumRats
    #         NumRats += AddRat
    #         printDelay(f'''\n\"Amazing! You got the answer right!\" the random rat says.\n\nOh, I didn't even say how many rat buddies were going to join you... Worry not, {AddRat} rats are joining you on your adventure!\"\n''')
    #         printDelay("\"I have soooooo many more riddles though. Do you want to answer another one? I'm sure I can scrounge up some more rat buddies if you answer right again!\"\n\nDo you want to answer more riddles to get more rat buddies or try and find more on your own?\n")
            
    #         while True:
    #             StopCont = input("1. Leave\n2. Try another riddle\n\nYour choice: ")
    #             if StopCont == '1':
    #                 printDelay(GiveUp)
    #                 give_up = True
    #                 break
    #             elif StopCont == '2':
    #                 printDelay(NewRiddle)
    #                 break
    #             else:
    #                 print("\nInput Error. Try again\n")
    #     elif guess == 'hint':
    #         printDelay(riddle['hint'])
    #     else:
    #         printDelay(WrongAsn)
    #         try:
    #             wrong_response = int(input(GiveTry))
    #         except ValueError:
    #             print("\nInput Error. Try again\n")
    #             continue
                
    #         if wrong_response == 1:
    #             printDelay(GiveUp)
    #             give_up = True
    #         elif wrong_response == 2:
    #             printDelay(TryAgain)
    #         else:
    #             print("\nInput Error. Try again\n")

# def Riddle():
#     AnsHint = "\n\nType out your guess or ask for a hint by typing 'hint'\n\n------------> "
#     WrongAsn = "\nNope, that wasn't the answer the rat was looking for... Do you want to give up? Or try again?\n"
#     GiveTry = "1. Give up\n2. Try again\n\nYour choice: "
 
#     printDelay('''As Steve continues on down the sewers, he's sees another rat scramble their way towards him.\n\n\"Hey! I heard you were looking to get a group of rats together! Me and my buddies are willing to join me if you can answer a riddle.\n\nSteve is always up for a challenge and agrees. \n\n\"Great! Here's a riddle for you:\"\n\n''')

#     give_up = False

#     while not give_up:
#         RiddleChoice = random.randint(1, 6)
#         RiddleChoice =1
#         if RiddleChoice == 1:
#             prYellow("What has a head and a tail but no body?")
#             Guess = str(input((AnsHint)))
#             if Guess.lower() == 'coin' or Guess.lower() == 'coins':
#                 RiddleCorrect()
#                 #break
#             elif Guess == 'hint':
#                 printDelay("You'll need to collect some of this if you want a movie ticket...\n")
#             else:
#                 printDelay(WrongAsn)
#                 while True:
#                     WrongResponse = int(input(GiveTry))
#                     if WrongResponse == 1:
#                         printDelay(GiveUp)
#                         give_up = True  # set the flag to True if user gives up
#                         break
#                     elif WrongResponse == 2:
#                         printDelay(TryAgain)
#                         break
#                     else:
#                         print("\nInput Error. Try again\n")
#         if RiddleChoice == 2:
#             prYellow("What starts with an E, ends with an E, but only contains one letter?")
#             Guess = str(input((AnsHint)))
#             if Guess.lower() == 'envelope' or Guess.lower() == 'envelopes':
#                 RiddleCorrect()
#                 #break
#             elif Guess == 'hint':
#                 printDelay("Humans send texts nowadays...\n")
#             else:
#                 printDelay(WrongAsn)
#                 while True:
#                     WrongResponse = int(input(GiveTry))
#                     if WrongResponse == 1:
#                         printDelay(GiveUp)
#                         give_up = True  # set the flag to True if user gives up
#                         break
#                     elif WrongResponse == 2:
#                         printDelay(TryAgain)
#                         break
#                     else:
#                         print("\nInput Error. Try again\n")
#         if RiddleChoice == 3:
#             prYellow("What has four legs in the morning, two legs in the afternoon, and three legs in the evening?")
#             Guess = str(input((AnsHint)))
#             if Guess.lower() == 'human' or Guess.lower() == 'humans':
#                 RiddleCorrect()
#                 #break
#             elif Guess == 'hint':
#                 printDelay("Steve will be trying to impersonate one of these later...\n")
#             else:
#                 printDelay(WrongAsn)
#                 while True:
#                     WrongResponse = int(input(GiveTry))
#                     if WrongResponse == 1:
#                         printDelay(GiveUp)
#                         give_up = True  # set the flag to True if user gives up
#                         break
#                     elif WrongResponse == 2:
#                         printDelay(TryAgain)
#                         break
#                     else:
#                         print("\nInput Error. Try again\n")       
#         if RiddleChoice == 4:
#             prYellow("What runs but never walks, has a mouth but never talks, has a bed \nbut never sleeps, has a head but never weeps?")
#             Guess = str(input((AnsHint)))
#             if Guess.lower() == 'a river' or Guess.lower() == 'river' or Guess.lower() == 'rivers':
#                 RiddleCorrect()
#                 #break
#             elif Guess == 'hint':
#                 printDelay("Rats are actually great swimmers! Maybe not in moving water though...\n")
#             else:
#                 printDelay(WrongAsn)
#                 while True:
#                     WrongResponse = int(input(GiveTry))
#                     if WrongResponse == 1:
#                         printDelay(GiveUp)
#                         give_up = True  # set the flag to True if user gives up
#                         break
#                     elif WrongResponse == 2:
#                         printDelay(TryAgain)
#                         break
#                     else:
#                         print("\nInput Error. Try again\n")
#         if RiddleChoice == 5:
#             prYellow("I am not alive, but I grow; I don't have lungs, but I need air; \nI don't have a mouth, but water kills me. What am I?")
#             Guess = str(input((AnsHint)))
#             if Guess.lower() == 'a fire' or Guess.lower() == 'fire' :
#                 RiddleCorrect()
#                 #break
#             elif Guess == 'hint':
#                 printDelay("Best to stay away when you see one. It's burned Steves fur a couple of times...\n")
#             else:
#                 printDelay(WrongAsn)
#                 while True:
#                     WrongResponse = int(input(GiveTry))
#                     if WrongResponse == 1:
#                         printDelay(GiveUp)
#                         give_up = True  # set the flag to True if user gives up
#                         break
#                     elif WrongResponse == 2:
#                         printDelay(TryAgain)
#                         break
#                     else:
#                         print("\nInput Error. Try again\n")
#         if RiddleChoice == 6:
#             prYellow("The more you look at it, the less you see. What is it?")
#             Guess = str(input((AnsHint)))
#             if Guess.lower() == 'darkness' or Guess.lower() == 'dark' :
#                 RiddleCorrect()
#                 #break
#             elif Guess == 'hint':
#                 printDelay("Steve can't see sometimes in the sewers. Especially at night...\n")
#             else:
#                 printDelay(WrongAsn)
#                 while True:
#                     WrongResponse = int(input(GiveTry))
#                     if WrongResponse == 1:
#                         printDelay(GiveUp)
#                         give_up = True  # set the flag to True if user gives up
#                         break
#                     elif WrongResponse == 2:
#                         printDelay(TryAgain)
#                         break
#                     else:
#                         print("\nInput Error. Try again\n")               



        


