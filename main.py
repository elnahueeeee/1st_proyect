### modulos ###
import random

### numero aleatorio ###
number = random.randint(1, 100)

### bucle principal ###
while True:

  ### pregunta al usuario ###
  print("adivina el numero del 1 al 100")
  guess = int(input())

  ### si el usuario acierta ###
  if guess == number:
    print("acertaste!")

    ### volver a intentar ###
    question = input("quieres intentar de nuevo? s/n ")
    if question == "s":
      number = random.randint(1, 100)

    else:
      question = input("quieres intentar de nuevo? s/n ")
  
  ### pistas ###
  elif guess < number:
    print("el numero es mas grande que", guess)
  
  elif guess > number:
    print("el numero es mas pequeño que", guess)
