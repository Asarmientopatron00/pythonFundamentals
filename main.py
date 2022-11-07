import numpy as np
import math 

options = {
  1: "Tijeras",
  2: "Papel",
  3: "Piedra",
}

rounds = 0
userWins = 0
pcWins = 0

print("""
  [ Welcome to Rock, Paper or Scissors ]
""")

maxRounds = int(input("Enter modality (3: better of 3 or 5: better of 5): "))
requiredToWin = math.ceil(maxRounds/2)

while userWins < requiredToWin and pcWins < requiredToWin:
  userInput = int(input("Selecciona una opción: {} :".format(str(options))))
  if (userInput not in options.keys()):
    print("Opción no válida")
    continue
  pcChoice = np.random.randint(1,4)
  if(userInput == pcChoice):
    print("Empate!")
    continue
  if(userInput < pcWins):
    if (pcWins - userInput == 2):
      pcWins+=1
      print("Punto para la PC")
    else:
      userWins+=1
      print("Punto para usted")
    continue
  if(userInput - pcWins == 2):
    userWins+=1
    print("Punto para usted")
  else:
    pcWins+=1
    print("Punto para la PC")
  
response = "Ha ganado {} con {} victorias".format("usted" if userWins>pcWins else "la computadora", max(userWins, pcWins))
print(response)
