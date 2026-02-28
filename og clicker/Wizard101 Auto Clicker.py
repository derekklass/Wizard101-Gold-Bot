'''
Wizard101 Farming Auto Clicker
----------
Created by Derek Klass
'''

# import clicking, key-pressing, and time-keeping modules
import pyautogui as pag
from pynput.keyboard import Controller
import time


# initiate any variables or classes
keyboard = Controller()

treasure_card = 5

# give time to close file explorer
time.sleep(5)

# repeat for all health potions
for i in range(5):
    # use the treasure card a specified number of times
    for position in range(treasure_card):
        # clicking each position to draw and use treasure card
        # draw button
        pag.moveTo(960, 619)
        time.sleep(0.3)
        pag.click()
        time.sleep(0.3)

        # tempest card
        pag.moveTo(940, 536)
        time.sleep(0.3)
        pag.click()

        # wait 30 seconds
        if position != (treasure_card - 1):
            time.sleep(20)

            # draw button
            pag.moveTo(960, 619)
            time.sleep(0.3)
            pag.click()
            time.sleep(0.3)

            # tempest card
            pag.moveTo(940, 536)
            time.sleep(0.3)
            pag.click()

            time.sleep(20)

        else:
            time.sleep(20)

    # exit the battle arena
    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')

    time.sleep(20)

    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')

    time.sleep(20)

    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')

    time.sleep(20)

    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')

    # backup normal tempest method in case there is still one minion left
    pag.moveTo(989, 532)
    time.sleep(0.3)
    pag.click()

    time.sleep(20)
    pag.click()

    # exit the battle arena again
    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')

    time.sleep(20)
    pag.click()

    keyboard.press('s')
    time.sleep(1.5)
    keyboard.release('s')

    # use the health potions
    pag.moveTo(165, 982)
    time.sleep(0.3)
    pag.click()

    # open the spells and make the treasure cards
    keyboard.press('p')
    time.sleep(0.3)
    keyboard.release('p')

    # storm spells
    pag.moveTo(803, 306)
    time.sleep(0.3)
    pag.click()

    # treasure cards
    pag.moveTo(610, 267)
    time.sleep(0.3)
    pag.click()

    # tempest card
    pag.moveTo(1060, 412)
    time.sleep(0.3)

    for i in range(38):
        pag.click()
        time.sleep(0.1)

    # close spellbook
    keyboard.press('p')
    time.sleep(0.3)
    keyboard.release('p')

    # go back into battle
    keyboard.press('w')
    time.sleep(15)
    keyboard.release('w')