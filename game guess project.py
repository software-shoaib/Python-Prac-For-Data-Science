import random

number = random.randint(1, 100)
attempt = 1
guess = int(input("guess the number: "))

while (True):
    if (guess>number):
        guess = int(input("guess another number, this one is too big: "))
        attempt +=1
    
    elif (guess<number):
        guess = int(input("guess another number, this one is too less: "))
        attempt +=1
    
    else:
        print (f"Yeah that's the number '{number}' you guessed it right in {attempt} attempts")
        break
