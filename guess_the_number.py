import random

correct = 'you guessed correctly!'
too_low = 'Too Low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))
        except ValueError:
            print('\n Must be an integer.')


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    x = 0
    while True:
        guess = get_guess()
        x = x +1
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            print('It took ' + str(x) + ' guesses.')
            break




if __name__ == '__main__':
    main()
