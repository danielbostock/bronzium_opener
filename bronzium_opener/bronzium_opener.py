#Start Import Area
from os import system, name 
from time import sleep 
import time, pyautogui
from bronzium_opener import text
import bronzium_opener
#End Import Area
  
# define our clear function 
def clear(): 
  
    # Windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # Unix Distros (Including MacOS)
    else: 
        _ = system('clear') 


def opener():
    print(text.INTRO)
    input('\nPress ENTER to continue...')
    clear()
    print(text.SELECTION)
    selection = int(input('Selection: '))
    clear()
    if selection == 1:
        cycle = 210
        cycles = 0
        while cycles == 0:
            cycles = int(input('Specify Cycles: '))
            cycle *= cycles
            timer = cycle
            timer_mins = timer
            timer_mins /= 60
            print('\nCurrent specified run time for the opener\nCycles: ' + str(cycles) + '\nTime: ' + str(timer) + ' seconds')
            confirm = int(input('\n\n1.Start\n2.Adjust run time for the opener\n3.Abort\n\nSelection: '))
            if confirm == 1:
                print(text.STARTING)
                print('\n\nThis pack opener will be running for ' + str(timer_mins) + ' minutes...' )
                time.sleep(5)
                
                while timer > 0:
                    pyautogui.press('1')
                    time.sleep(1.5)
                    timer -= 1.5



