from random import randint
import time

def Answer_checker(Answer, Guess):
  position = int(0)
  clue = ""
  for number in Guess:
    if number == Answer[position]:
      clue += "G"
    elif number in Answer:
      clue += "C"
    else:
      clue += "-"
    position += 1
  print(clue)
  return clue == "GGGGG"

range_start = 10**(5-1)
range_end = (10**5)-1


answer = str(randint(range_start, range_end))

mastermind = """  
                     _                      _           _ 
                    | |                    (_)         | |
 _ __ ___   __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |
| '_ ` _ \ / _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
| | | | | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
|_| |_| |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|

"""


print("Welcome to MasterMind!\n")


no_of_guesses = 0
guessed_correctly = False


while True:
  print("Type HTO If You Would Like To See How To Play or Type P If You Would Like To Start A Game!")
  menu1 = input("")
  if menu1.upper() == "HTO":
    print("The rules of the game are simple, you have 6 guesses and only 6 to find out the 5 digit code.\n If the number you guess is in the correct place...a G will be placed on the spot of the number.\n If the Number you guess is in the answer but the wrong place...a C will be palced on the spot of the number. \n If the number you guess is not in the answer at all...a - will be placed on the spot of the number.")
    time.sleep(8)
  if menu1.upper() == "P":
    print("Time To Enter...MasterMind")
    time.sleep(2)
    break
  

while no_of_guesses < 6 and not guessed_correctly:

  guess = input("Input a 5 digit Number and Press enter: \n")
  print("You have guessed", guess)
  no_of_guesses += 1

  guessed_correctly = Answer_checker(answer, guess)

  if guessed_correctly:
    print("Congratulations! You guess the correct work in", no_of_guesses, "tries!")
  else:
    print("You have used up all your guesses...the correct word is", answer)