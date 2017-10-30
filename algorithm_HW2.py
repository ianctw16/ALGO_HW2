import time
import random
import tkinter as tk
from tkinter import LEFT, BOTTOM, RIGHT, TOP

window = tk.Tk()
window.title('-------------2*5 #c Game-------------')
window.configure(background='light yellow')
# window.geometry('600x400')


def c_game(response):
    global pool_2
    global guess_1, guess_2
    if(response == '2c'):
        # print('Correct. So the answer is', guess_1, guess_2)
        var_system_ask_1.set('Correct. The number is')
        var_system_ask_2.set(guess_1)
        var_system_ask_3.set(guess_2)
        var_system_ask_4.set('')
        print('Correct. The number is', guess_1, guess_2)

    elif(response == '1c'):
        # removeing node = [guess_1, guess_2]
        i = 0
        while(i < len(pool_2)):
            if(guess_1 in pool_2[i] and guess_2 in pool_2[i]):
                # print('del', pool_2[i])
                pool_2.remove(pool_2[i])
                break
            else:
                i = i + 1

        # removeing node don't have guess_1 or guess_2.
        i = 0
        while(i < len(pool_2)):
            if(guess_1 not in pool_2[i] and guess_2 not in pool_2[i]):
                # print('del', pool_2[i])
                pool_2.remove(pool_2[i])
                i = 0
            else:
                i = i + 1

        test = random.randrange(0, len(pool_2))
        guess_1 = pool_2[test][0]
        guess_2 = pool_2[test][1]
        ask_ans()

    elif(response == '0c'):
        i = 0
        while(i < len(pool_2)):
            if(guess_1 in pool_2[i] or guess_2 in pool_2[i]):
                # print('del', pool_2[i])
                pool_2.remove(pool_2[i])
                i = 0
            else:
                i = i + 1

        test = random.randrange(0, len(pool_2))
        guess_1 = pool_2[test][0]
        guess_2 = pool_2[test][1]
        ask_ans()


def ask_ans():
    global guess_1, guess_2
    # print('Candidate:', pool_2)
    var_candidate.set(pool_2)
    # print('is(', guess_1, guess_2, ')?')
    var_system_ask_2.set(guess_1)
    var_system_ask_3.set(guess_2)
    print('asked:', guess_1, guess_2)
    # response = input(">>> Ans(2c, 1c, 0c): ")
    # c_game(response, guess_1, guess_2)


# Candidate Label
f_top = tk.Frame(window)
f_top.pack(side=TOP)
var_candidate_2 = tk.StringVar()
var_candidate_2.set('Candidates: ')
var_candidate = tk.StringVar()
l_candidate = tk.Label(f_top,
                       textvariable=var_candidate,
                       font=("Comic Sans MS", 12),
                       bg='deep sky blue')
l_candidate_2 = tk.Label(f_top,
                         textvariable=var_candidate_2,
                         font=("Comic Sans MS", 12),
                         bg='deep sky blue')
l_candidate_2.pack(side=LEFT)
l_candidate.pack(side=LEFT)


# System Ask Label
f_top_2 = tk.Frame(window, bg='light yellow')
f_top_2.pack(side=TOP)

var_system_ask_1 = tk.StringVar()
var_system_ask_1.set('Your number is(')
var_system_ask_2 = tk.StringVar()
var_system_ask_3 = tk.StringVar()
var_system_ask_4 = tk.StringVar()
var_system_ask_4.set(')?')

l_system_ask_1 = tk.Label(f_top_2,
                          textvariable=var_system_ask_1,
                          font=("Comic Sans MS", 14),
                          bg='light yellow')
l_system_ask_2 = tk.Label(f_top_2,
                          textvariable=var_system_ask_2,
                          font=("Comic Sans MS", 18),
                          bg='green yellow')
l_system_ask_3 = tk.Label(f_top_2,
                          textvariable=var_system_ask_3,
                          font=("Comic Sans MS", 18),
                          bg='green yellow')
l_system_ask_4 = tk.Label(f_top_2,
                          textvariable=var_system_ask_4,
                          font=("Comic Sans MS", 14),
                          bg='light yellow')
l_system_ask_1.pack(side=LEFT)
l_system_ask_2.pack(side=LEFT)
l_system_ask_3.pack(side=LEFT)
l_system_ask_4.pack(side=LEFT)


def restart():
    print('---------------restart---------------')
    global pool_2, guess_1, guess_2
    pool_2 = []
    for i in range(0, 5):
        for j in range(i+1, 5):
            pool_2.append([i, j])

    random.seed(time.time())
    test = random.randrange(0, len(pool_2))
    # print()
    guess_1 = pool_2[test][0]
    guess_2 = pool_2[test][1]
    print('log: ')
    var_system_ask_1.set('Your number is(')
    var_system_ask_4.set(')?')
    ask_ans()


pool_2 = []
for i in range(0, 5):
    for j in range(i+1, 5):
        pool_2.append([i, j])


random.seed(time.time())
test = random.randrange(0, len(pool_2))
# print()
guess_1 = pool_2[test][0]
guess_2 = pool_2[test][1]
print('log: ')
ask_ans()
'''
# Answer Buttons
c2_button = tk.Button(window,
                      text='2c',
                      command=c_game('2c', guess_1, guess_2))
c1_button = tk.Button(window,
                      text='1c',
                      command=c_game('1c', guess_1, guess_2))
c0_button = tk.Button(window,
                      text='0c',
                      commmad=c_game('0c', guess_1, guess_2))
c2_button.pack()
c1_button.pack()
c0_button.pack()
'''


def e_submit():
    ans = e.get()
    # print(guess_1, guess_2)
    c_game(ans)


'''
img = tk.PhotoImage(file='submit_button.png')
img.width = 74
img.height = 18
'''
f_bot = tk.Frame(window, bg='light yellow')
f_bot.pack(side=BOTTOM)
l_e = tk.Label(f_bot, text='A(2c,1c,0c):',
               font=("Comic Sans MS", 14),
               bg='light yellow')
e = tk.Entry(f_bot)
e_button = tk.Button(f_bot,
                     text='submit',
                     bg='gold',
                     font=("Comic Sans MS", 16),
                     command=e_submit)
restart_button = tk.Button(window,
                           text='RE',
                           bg='brown1',
                           font=("Comic Sans MS", 20),
                           command=restart)
l_e.pack(side=LEFT)
e_button.pack(side=RIGHT)
e.pack(side=RIGHT)
restart_button.pack()
window.mainloop()
