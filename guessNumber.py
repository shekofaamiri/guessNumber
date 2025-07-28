import random

try:
    low = int(input('enter lower bound:\n'))
    high = int(input('enter high bound:\n'))
except ValueError:
    print("Please enter valid integers for bounds.")
    exit()

r = random.randint(low, high)
guess_count = 5

while guess_count > 0:
    try:
        new_guess = int(input('enter your new guess:\n'))
    except ValueError:
        print('Please enter a valid number')
        continue

    if r == new_guess:
        print('Great! Your guess is correct.')
        break
    elif r > new_guess:
        print('Your guess is lower than the number.')
    else:
        print('Your guess is higher than the number.')

    guess_count -= 1

if guess_count == 0:
    print(f'Sorry, you lost. The number was {r}.')
