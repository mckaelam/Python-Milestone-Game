import func

func.CityChoice()


# func.PrintDelay(func.Intro)
# print (func.Line)
# func.Wait()
# func.PrintDelay(func.Instructions)
# print (func.Line)
# func.Wait()

# func.PrintDelay(func.StartPoint)
# SewerBool = False
# CityBool = False

# while True:
#     if SewerBool is False and CityBool is False:
#         func.PrintYellow("+---------------------------+\n| 1. Go to the sewers        |\n| 2. Go to the city          |\n| 3. Go to the movie theatre |\n| 4. Check inventory         |\n+---------------------------+\n")
#         try:
#             choice = int(input("Your Choice: "))
#         except ValueError:
#             func.PrintRed("Invalid input. Please enter a number.")
#             continue
#         if choice < 1 or choice > 4:
#             func.PrintRed("Invalid input. Please enter a valid number.")
#         if choice == 1:
#             SewerBool = True
#             func.SewerChoice()
#         elif choice == 2:
#             CityBool = True
#             func.CityChoice()
#         elif choice == 3:
#             func.GoMovie()
#             break
#         elif choice == 4:
#             func.CheckInv()
#     elif SewerBool is False and CityBool is True:
#         func.PrintYellow("+---------------------------+\n| 1. Go to the sewers        |\n| 2. Go to the movie theatre |\n| 3. Check inventory         |\n+---------------------------+\n")
#         try:
#             choice = int(input("Your Choice: "))
#         except ValueError:
#             func.PrintRed("Invalid input. Please enter a number.")
#             continue
#         if choice < 1 or choice > 3:
#             func.PrintRed("Invalid input. Please enter a valid number.")
#         if choice == 1:
#             SewerBool = True
#             func.SewerChoice()
#         if choice == 2:
#             func.GoMovie()
#             break
#         if choice == 3:
#             func.CheckInv()

#     elif SewerBool is True and CityBool is False:
#         func.PrintYellow("+---------------------------+\n| 1. Go to the city          |\n| 2. Go to the movie theatre |\n| 3. Check inventory         |\n+---------------------------+\n")
#         try:
#             choice = int(input("Your Choice: "))
#         except ValueError:
#             func.PrintRed("Invalid input. Please enter a number.")
#             continue
#         if choice < 1 or choice > 3:
#             func.PrintRed("Invalid input. Please enter a valid number.")            
#         if choice == 1:
#             CityBool = True
#             func.CityChoice()
#         if choice == 2:
#             func.GoMovie()
#             break
#         if choice == 3:
#             func.CheckInv()
#     else:
#         func.PrintYellow("+---------------------------+\n| 1. Go to the movie theatre |\n| 2. Check inventory         |\n+---------------------------+\n")
#         try:
#             choice = int(input("Your Choice: "))
#         except ValueError:
#             func.PrintRed("Invalid input. Please enter a number.")
#             continue
#         if choice < 1 or choice > 2:
#             func.PrintRed("Invalid input. Please enter a valid number.")
#         if choice == 1:
#             func.GoMovie()
#             break
#         if choice == 2:
#             func.CheckInv()
