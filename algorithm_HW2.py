import time
import random

pool = [0, 1, 2, 3, 4]
pool_2 = []
for i in range(0, 5):
    for j in range(i+1, 5):
        pool_2.append([i, j])


def c_game(response, guess_1, guess_2):
    if(response == '2c'):
        print('Correct. So the answer is', guess_1, guess_2)

    elif(response == '1c'):
        # removeing node = [guess_1, guess_2]
        for i in range(0, len(pool_2)):
            if(guess_1 and guess_2 in pool_2[i]):
                pool_2.remove[i]
        # removeing node don't have guess_1 or guess_2.
        for i in range(0, len(pool_2)):
            while(guess_1 or guess_2 not in pool_2[i]):
                pool_2.remove[i]

    elif(response == '0c'):
        pool.remove(guess_1)
        pool.remove(guess_2)

        while(len(pool) <= 1):
            print('Ur answer is WRONG!!!!!!')
            exit()

        new_guess_1 = pool[random.randrange(0, len(pool))]
        new_guess_2 = pool[random.randrange(0, len(pool))]

        while(new_guess_1 == new_guess_2):
            new_guess_1 = pool[random.randrange(0, len(pool))]

        ask_ans(new_guess_1, new_guess_2)


def ask_ans(guess_1, guess_2):
    print('is', guess_1, guess_2, '?')
    response = input(">>> A(2c, 1c, 0c): ")
    c_game(response, guess_1, guess_2)


random.seed(time.time())
guess_1 = pool[random.randrange(0, len(pool))]
guess_2 = pool[random.randrange(0, len(pool))]

while(guess_2 == guess_1):
    guess_2 = pool[random.randrange(0, len(pool))]

ask_ans(guess_1, guess_2)
