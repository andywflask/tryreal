import time
import pyperclip
import pyautogui as pt
import random

rare = ["cm.png", "st.png", "cb.png"]
time_run = 0.5


# pt.locateOnScreen(random.choice(rare)
def add_players_rare():
    try:
        pt.moveTo(pt.locateOnScreen("lb.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(1.5)
        print(000)

    except pt.ImageNotFoundException:
        pt.moveTo(pt.locateOnScreen("ctry.png", confidence=.92), duration=.5)
        pt.click()
        time.sleep(time_run)
    try:
        pt.moveTo(pt.locateOnScreen("addplayer.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        print(000)

    except pt.ImageNotFoundException:

        pt.moveTo(pt.locateOnScreen("swap.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        print(000)

    try:
        pt.locateOnScreen("rare.png", confidence=.8)
        print(111)

    except pt.ImageNotFoundException:

        pt.moveTo(pt.locateOnScreen("common.png", confidence=.8), duration=.5)
        print(222)

        pt.click()
        time.sleep(time_run)
        pt.moveTo(pt.locateOnScreen("rare2.png", confidence=.8), duration=.5)
        print(333)

        pt.click()
        time.sleep(time_run)
    else:
        pass
    try:
        pt.moveTo(pt.locateOnScreen("exclude.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        pt.moveTo(pt.locateOnScreen("highest.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        pt.moveTo(pt.locateOnScreen("low.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        pt.moveTo(pt.locateOnScreen("position.png", confidence=.9), duration=.5)
        pt.click()
        time.sleep(time_run)
    except pt.ImageNotFoundException:
        pass
    pt.moveTo(pt.locateOnScreen("search.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(1.5)
    pt.moveTo(pt.locateOnScreen("add.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(1.5)


def add_players_common():
    pt.moveTo(pt.locateOnScreen("lb.png", confidence=.95), duration=.5)
    pt.click()
    time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("addplayer.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(time_run)
    try:
        pt.locateOnScreen("common.png", confidence=.8) is None
    except pt.ImageNotFoundException:
        print(111)
        pt.moveTo(pt.locateOnScreen("rare.png", confidence=.8), duration=.5)
        print(222)
        pt.click()
        time.sleep(time_run)
        pt.moveTo(pt.locateOnScreen("common2.png", confidence=.8), duration=.5)
        print(333)

        pt.click()
        time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("exclude.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("highest.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("low.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("position.png", confidence=.9), duration=.5)
    pt.click()
    time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("search.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(1)
    pt.moveTo(pt.locateOnScreen("add.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(1.5)
    try:
        pt.locateOnScreen("lb.png", confidence=.8)
        add_players_common()
    except pt.ImageNotFoundException:

        pass

    time.sleep(time_run)


def squad_builder():
    time.sleep(0.5)
    pt.moveTo(pt.locateOnScreen("builder.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(time_run)

    # pt.moveTo(pt.locateOnScreen("untrade.png", confidence=.8), duration=.5)
    # pt.click()
    # time.sleep(time_run)
    try:
        pt.moveTo(pt.locateOnScreen("rarity.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        pt.moveTo(pt.locateOnScreen("common2.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
        try:
            pt.moveTo(pt.locateOnScreen("ignore.png", confidence=.8), duration=.5)
            pt.click()
            time.sleep(time_run)

        except pt.ImageNotFoundException:
            pass


    except pt.ImageNotFoundException:
        pass
    pt.scroll(-1000)
    time.sleep(time_run)
    pt.moveTo(pt.locateOnScreen("build.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(1.5)


def sbc():
    time.sleep(1)
    pt.moveTo(pt.locateOnScreen("82.png", confidence=.8), duration=.5)
    print("moved")
    pt.click()
    time.sleep(1)
    squad_builder()

    add_players_rare()
    add_players_rare()

    try:
        pt.moveTo(pt.locateOnScreen("submit.png", confidence=.8), duration=.5)
        pt.click()
        time.sleep(time_run)
    except:
        add_players_common()
        try:
            pt.moveTo(pt.locateOnScreen("submit.png", confidence=.8), duration=.5)
            pt.click()

        except pt.ImageNotFoundException:

            pt.moveTo(pt.locateOnScreen("require.png", confidence=.8), duration=.5)
            pt.click()
            time.sleep(time_run)
            add_players_common()
            pt.moveTo(pt.locateOnScreen("submit.png", confidence=.8), duration=.5)
            pt.click()
        time.sleep(4.5)

    pt.moveTo(pt.locateOnScreen("claim1.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(.6)
    pt.moveTo(pt.locateOnScreen("claim1.png", confidence=.8), duration=.5)
    pt.click()
    time.sleep(.6)
    sbc()


sbc()
