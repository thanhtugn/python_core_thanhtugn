import random 
from loguru import logger

attempts_list = []
def show_score():
    if not attempts_list:
        logger.info("Haven't played any games yet")
    else:
        logger.info(f"Best score: {max(attempts_list)}")

def start_game():
    attempts = 0
    random_number = random.randint(1, 10)
    logger.info('--WELCOME TO GAME--')
    player = input('Enter your name: ')
    wanna_play = input(f'HI{player}, u ready ?? (y/n): ')

    while wanna_play.lower() == 'y':
        guess  = int(input('Guess a number between 1 and 10: '))
        if guess >10 or guess < 0:
            logger.error('Please enter a number between 1 and 10')
            continue
        attempts += 1

        if guess == random_number:
            logger.info('Congratulations! You r correct!')
            attempts_list.append(attempts)
            wanna_play = input('Would you like to play again? (y/n): ')
            if wanna_play == 'y':
                random_number = random.randint(1, 10)
                attempts = 0
            else:
                show_score()
        elif guess < random_number:
            logger.info('IT IS LOWER')
        else:
             logger.info('IT IS HIGHER')

if __name__ == '__main__':
    start_game()