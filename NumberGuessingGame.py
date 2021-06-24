import random
randomDigit=int(random.randint(1,9))
lives=5
val=0
state='playing'

while( state == 'playing'):

    answer=int(input('\n'"Type your answer: "))

    if answer>randomDigit:
        lives=lives-1
        print("","Hint : (Try gusseing a smaller digit)",'\n',"lives :",lives)
    else:
        if answer<randomDigit:
            lives=lives-1
            print("","Hint : (Try gusseing a bigger digit)",'\n',"lives :",lives)

    if answer == randomDigit:
        state='end'
        print('\n'"You Won"'\n')

    if(lives == val):
        state='end'
        print('\n'"You loss"'\n')