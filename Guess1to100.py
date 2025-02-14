from random import randint

num = randint(1, 100)

guess_num = 0
print("Guess a number between 1 and 100")

while True:
	guess = int(input(": "))
	guess_num += 1
	
	if guess > num:
		print("Too high")
	elif guess < num:
		print("Too low")
	elif guess == num:
		break

print("You Win! the Number was", num)
print(f"it took you: {guess_num} tries.")