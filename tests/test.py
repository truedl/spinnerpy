from random import randint
from time import sleep
import spinner

def FirstProgress():
    sleep(2)

def SecondProgress(number):
    sleep(2)
    print(f'\nNumber {number} was provided')

spinner.Spinner('default').start(progress=FirstProgress, text='First Progress in progress... ')
print('\nDONE')
spinner.Spinner('dots').start(progress=SecondProgress, args=[randint(1, 10)], text='Seconds Progress in progress... ')
print('DONE')