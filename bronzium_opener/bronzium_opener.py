#Start Import Area
from os import system, name 
from time import sleep 
import time, pyautogui
from bronzium_opener import text
import bronzium_opener
#End Import Area

print(text.INTRO)
input('\nPress ENTER to continue...')


def clear(): 
  
    # Windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # Unix Distros (Including MacOS)
    else: 
        _ = system('clear') 


def opener():
    clear()
    print(text.SELECTION)
    selection = int(input('Selection: '))
    clear()
    if selection == 1:
        cycle = 210
        cycles = 0
        while cycles == 0:
            print(text.MENU_CYCLES_TOP)
            cycles = int(input('Specify Cycles: '))
            cycle *= cycles
            timer = cycle
            timer_mins = timer
            timer_mins /= 60
            timer_hrs = timer_mins
            timer_hrs /= 60
            clear()
            print(text.MENU_CYCLES_RUNTIME)
            print('\nCycles: ' + str(cycles) + '\nMinutes: ' + str(timer_mins) + '\nHours: ' + str(round(timer_hrs, 2)))
            print(text.MENU_GEN_BREAK)
            confirm = int(input(text.CONFIRM))
            if confirm == 1:
                print(text.STARTING)
                print('\n\nThis pack opener will be running for ' + str(timer_mins) + ' minutes...' )
                time.sleep(5)
                while timer > 0:
                    pyautogui.press('1')
                    time.sleep(1.5)
                    timer -= 1.5
            elif confirm == 2:
                clear()
                cycles = 0
            else:
                input(text.ERROR_GENERAL_INVALID_SELECTION)
                clear()
                opener()
                
    elif selection == 2:
        timer_mins = 0
        while timer_mins == 0:
            print(text.MENU_TIME_TOP)
            timer = False
            while timer == False:
                timer = int(input('\nWould you like to specify hours or minutes?\n\n1. Minutes\n2. Hours\n\nSelection: '))
                if timer == 1:                
                    timer_mins = int(input(text.TIMER_MINS))
                    timer_secs = timer_mins
                    timer_secs *= 60
                    timer_hrs = timer_mins
                    timer_hrs /= 60
                    clear()
                    print(text.MENU_TIME_RUNTIME)
                    print('Minutes: ' + str(timer_mins) + '\nHours: ' + str(round(timer_hrs,2)))
                    print(text.MENU_GEN_BREAK)
                    confirm = int(input(text.CONFIRM))
                    if confirm == 1:
                        print(text.STARTING)
                        print('\n\nThis pack opener will be running for ' + str(timer_mins) + ' minutes...' )
                        time.sleep(5)
                        while timer_secs > 0:
                            pyautogui.press('1')
                            time.sleep(1.5)
                            timer_secs -= 1.5
                    elif confirm == 2:
                        clear()
                        timer_mins = 0
                    else:
                        input(text.ERROR_GENERAL_INVALID_SELECTION)
                        clear()
                        opener()
                if timer == 2:
                    timer_hrs = int(input(text.TIMER_HOURS))
                    timer_secs = timer_hrs
                    timer_secs *= 3600
                    timer_mins = timer_hrs
                    timer_mins *= 60
                    clear()
                    print(text.MENU_TIME_RUNTIME)
                    print('Minutes: ' + str(timer_mins) + '\nHours: ' + str(round(timer_hrs,2)))
                    print(text.MENU_GEN_BREAK)
                    confirm = int(input(text.CONFIRM))
                    if confirm == 1:
                        print(text.STARTING)
                        print('\n\nThis pack opener will be running for ' + str(timer_mins) + ' minutes...' )
                        time.sleep(5)
                        while timer_secs > 0:
                            pyautogui.press('1')
                            time.sleep(1.5)
                            timer_secs -= 1.5
                    elif confirm == 2:
                        clear()
                        timer_mins = 0
                    else:
                        input(text.ERROR_GENERAL_INVALID_SELECTION)
                        clear()
                        opener()
    elif selection == 3:
        print('PLACEHOLDER')
        clear()
        opener()
    else:
        input(text.ERROR_GENERAL_INVALID_SELECTION)
        clear()
        opener()


            



