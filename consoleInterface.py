from PostitClass import *
import PostitManager
import PostitRenderer
import sys

def exit(errCode):
  print("\nExiting the program... \nHave a Nice day!")
  sys.exit(errCode)

#to be run on startup
def startup():
  #get action
  print("What would you like to do? (1, 2, 3, 4)")
  decision = input("1: New Note \n2: Last Note \n3: Load Note \n4: Exit \n")
  print("\n")

  if (decision == "1") | (decision.lower() == "New Note".lower()):
    print("Creating New Note...")
    newNote = Postit("red", "blue", "")
  elif (decision == "2") | (decision.lower() == "Last Note".lower()):
    print("Loading Last note...")
  elif (decision == "3") | (decision.lower() == "Load Note".lower()):
    print("Previewing All Notes...")
  elif (decision == "4") | (decision.lower() == "Exit".lower()):
    exit(0)
  else:
    print("\nInvalid Selection! Please pick a selection either in number or in name!")

continueLoop = True

while continueLoop:
  startup()
  continueLoop = input("\nwould you like to exit the program? (y/n)): ").lower() == "n"
  print("\n")