correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

guess = input ("Noman says: Can you guess my planet? >>> ")


if guess == planet:
    print("Congratulations!, You guessed right planet")
else: 
    print("You are wrong")