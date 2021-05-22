import time, pyautogui

def opener(timer):

    print('Starting The Bronzium Pack Opener in 5 Seconds...')
    time.sleep(5)
    print('\nPack opening has now begun and will run for ' + str(timer) + ' seconds')

    while timer > 0:
        pyautogui.press('1')
        time.sleep(1.5)
        timer -= 1.5



