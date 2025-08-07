fruits=['banana','orange','grapes','mango','cherrry','peach']

import random
secret_fruit = random.choice(fruits)
print('welcome to fruit guessing game !')

print('Im thinking of a fruit can u guess which one? ')

guess = ""
attempts = 0

while guess != secret_fruit:
    guess = input('your guess :')
    attempts+=1

    if guess == secret_fruit:
        print("u got it correct")

    else:
        print("nope your answer is incorrect")