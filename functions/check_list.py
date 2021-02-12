from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2:  ")
    return int(guess)  

def check_guess(mylist):
    guess = player_guess()
    shuffled = shuffle_list(mylist)
    if shuffled[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)

print(check_guess(mylist=[' ','O',' ']))