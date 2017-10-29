import time
import random

pool_2 = []
for i in range(0, 5):
    for j in range(i+1, 5):
        pool_2.append([i, j])


def c_game(response, guess_1, guess_2):
    if(response == '2c'):
        print('Correct. So the answer is', guess_1, guess_2)

    elif(response == '1c'):
        # removeing node = [guess_1, guess_2]
        i = 0
        while(i < len(pool_2)):
            if(guess_1 in pool_2[i] and guess_2 in pool_2[i]):
                print('del', pool_2[i])
                pool_2.remove(pool_2[i])
                break
            else:
                i = i + 1

        # removeing node don't have guess_1 or guess_2.
        i = 0
        while(i < len(pool_2)):
            if(guess_1 not in pool_2[i] and guess_2 not in pool_2[i]):
                print('del', pool_2[i])
                pool_2.remove(pool_2[i])
                i = 0
            else:
                i = i + 1

        test = random.randrange(0, len(pool_2))
        guess_1 = pool_2[test][0]
        guess_2 = pool_2[test][1]

        ask_ans(guess_1, guess_2)

    elif(response == '0c'):
        i = 0
        while(i < len(pool_2)):
            if(guess_1 in pool_2[i] or guess_2 in pool_2[i]):
                print('del', pool_2[i])
                pool_2.remove(pool_2[i])
                i = 0
            else:
                i = i + 1

        test = random.randrange(0, len(pool_2))
        guess_1 = pool_2[test][0]
        guess_2 = pool_2[test][1]

        ask_ans(guess_1, guess_2)


def ask_ans(guess_1, guess_2):
    print('Candidate:', pool_2)
    print('is(', guess_1, guess_2, ')?')
    response = input(">>> Ans(2c, 1c, 0c): ")
    c_game(response, guess_1, guess_2)


random.seed(time.time())
test = random.randrange(0, len(pool_2))
print()
guess_1 = pool_2[test][0]
guess_2 = pool_2[test][1]
print('-------------2*5 #c Game-------------')
ask_ans(guess_1, guess_2)
