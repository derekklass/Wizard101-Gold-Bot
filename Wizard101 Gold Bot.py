"Created by Derek Klass - Wizard101 Gold Bot"

# import clicking and image locating module
import pyautogui as pag
import time


# repeat continuously
while(True):

    # press x
    pag.keyDown('x')
    time.sleep(0.1)
    pag.keyUp('x')

    # wait 20 seconds
    time.sleep(20)

    # hold w for 3 seconds
    pag.keyDown('w')
    time.sleep(3)
    pag.keyUp('w')

    # wait 10 seconds
    time.sleep(10)

    # click on epic card
    pag.moveTo(pag.locateCenterOnScreen('epic.jpg'))
    time.sleep(0.1)
    pag.click()

    # wait 0.1 seconds
    time.sleep(0.1)

    # click on tempest card
    pag.moveTo(pag.locateCenterOnScreen('tempest.jpg'))
    time.sleep(0.1)
    pag.click()

    # wait 0.1 seconds
    time.sleep(0.1)

    # click inbetween epic and tempest cards
    pag.moveTo(992, 530)
    time.sleep(0.1)
    pag.click()

    # wait for 45 seconds
    time.sleep(45)

    # hold a for 0.6 seconds
    pag.keyDown('a')
    time.sleep(0.6)
    pag.keyUp('a')

    # wait 0.5 seconds
    time.sleep(0.5)

    # hold w for 4 seconds
    pag.keyDown('w')
    time.sleep(4)
    pag.keyUp('w')

    # wait 15 seconds
    time.sleep(15)

    # hold s for 1 second
    pag.keyDown('s')
    time.sleep(1)
    pag.keyUp('s')