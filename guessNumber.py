secret_number = 9
guess_counts = 0

while guess_counts <= 3:
    guess = int(input("Enter the guess: "))
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, You failed")
