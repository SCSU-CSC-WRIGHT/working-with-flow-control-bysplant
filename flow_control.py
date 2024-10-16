import random
number = random.randint (1,10)
attempts = 3
count = 1
while count <= attempts:
    guess = int(input("Guess the number between 1-10 "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("You win!")
        break
    count += 1
print("You lose")
    

# Lab 2
num = int(input("Enter a number to start a countdown "))
count = num
while count != 0:
    print(count)
    count -= 1

# Lab 3
total = 0
num = int(input("Enter a number "))
for sum in range(1, num + 1):
    total += sum
print(total)
    