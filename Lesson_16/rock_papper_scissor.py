import random
from loguru import logger

def check_player_status():
    user_play = input("Would you like to play more? (y/n): ")
    if user_play.lower == 'y':
        return True
    elif user_play.lower == 'n':
        return False
    else:
        logger.info("Invalid input. Please try again.")

def play_game():
    play = True
    player = input("Enter your name: ")
    logger.info(f'WELCOME {player} TO THE GAME')
    while play:
        user_choice = input(f'Please select one: [R]OCK, [P]APER, [S]CISSORS : ')
        if user_choice not in ['R', 'P', 'S']:
            logger.error(f'Invalid weapon, please select again')
        else:
            com_choice = random.choice(['R', 'P', 'S'])
            logger.info(f'Computer chose {com_choice}')
            if user_choice == com_choice:
                logger.info('TIE')
            elif user_choice.upper == 'R' and com_choice.upper == 'P':
                logger.info('Computer wins')
            elif user_choice.upper == 'R' and com_choice.upper == 'S':
                logger.info('You win')
            elif user_choice.upper == 'P' and com_choice.upper == 'R':
                logger.info('You win')
            elif user_choice.upper == 'P' and com_choice.upper == 'S':
                logger.info('Computer wins')
            elif user_choice.upper == 'S' and com_choice.upper == 'R':
                logger.info('Computer win')
            else:
                user_choice.upper == 'S' and com_choice.upper == 'P'
                logger.info('You wins')

        play = check_player_status()
        logger.info('--Game over--')
if __name__ == '__main__':
    play_game()