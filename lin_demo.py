from random import randint

random_number = random(0, 100)
print ('random_number')
lives>=1

while lives >0
    guess_number = int(input('guess the number'))
    if random_number == guess_number:
        print ('you are correct')
        break
        lives-=1
        print('game over')