import random

correct = '\nYou guessed correctly!'
too_low = 'Too Low'
too_high = 'Too High'



def configure_range():
    '''Set the high and low values for the random number'''
    print("\nSpecify the range of the random number generated")
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    return x, y


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('\nGuess the secret number? '))
        except ValueError:
            print('\nMust be an integer.')


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
        x = x + 1
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            print('It took ' + str(x) + ' guesses.')
            playAgain = input("\nWould you like to play again? (y/n) ")
            if playAgain == "y" or "Y":
                (low, high) = configure_range()
                secret = generate_secret(low, high)
                x = 0
                continue
            else:
                break




if __name__ == '__main__':
    main()
