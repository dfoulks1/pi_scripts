import gpiozero
import threading
import time
import random
import os
from subprocess import call

speed = 0.25
sound = True

displaying = False
is_won_cur_lvl = False
is_game_over = False

# Game State
current_level = 1
current_step_of_level = 0
pattern = []


colors = ["blue", "red", "green", "yellow"]
buzzer = gpiozero.TonalBuzzer(23)
simon = {
    "blue": {
        "button": gpiozero.Button(12),
        "led": gpiozero.LED(6),
        "tone": gpiozero.tones.Tone("E3")
        },
    "red": {
        "button": gpiozero.Button(16),
        "led": gpiozero.LED(13),
        "tone": gpiozero.tones.Tone("A4")
        },
    "green": {
        "button": gpiozero.Button(20),
        "led": gpiozero.LED(19),
        "tone": gpiozero.tones.Tone("E4")
        },
    "yellow": {
        "button": gpiozero.Button(21),
        "led": gpiozero.LED(26),
        "tone": gpiozero.tones.Tone("Cs4")
        },
    }

def add_color_to_pattern():
    global is_won_cur_lvl, current_step_of_level
    is_won_cur_lvl = False
    current_step_of_level - 0
    c = random.randint(0, 3)
    patern.append(colors[c])

def display_pattern():
    global displaying
    displaying = True
    for i in range(current_level):
        buzzer.play(simon[pattern[i]]["tone"])
        simon[pattern[i]]["led"].on()
        time.sleep(speed)
        simon[pattern[i]]["led"].off()
        time.sleep(speed)
    displaying = False

def player_turn():
    while not is_won_cur_lvl and not is_game_over:
        time.sleep(0.1)
        
def reset():
    global displaying, is_won_cur_lvl, is_game_over
    global current_level, current_step_of_level, pattern
    
    displaying = False
    is_won_cur_lvl = False
    is_game_over = False

    current_level = 1
    current_step_of_level = 0
    pattern = []
        
def start_game():
    while True:
        add_color_to_pattern()
        display_pattern()
        player_turn()
        if is_game_over:
            print("Game Over! Your Score was {}\n".format(current_level+1))
            play_again = input("Press 'Y' to play again")
            if play_again.lower == "y":
                reset()
                print("Start new round!!\n")
            else:
                print("Thanks for playing\n")
                break
        time.sleep(2)
        
def init_game():
    # Set Callbacks
    simon["blue"]["button"].when_pressed = simon["blue"]["led"].on()
    simon["blue"]["button"].when_released = simon["blue"]["led"].off()
    simon["red"]["button"].when_pressed = simon["red"]["led"].on()
    simon["red"]["button"].when_released = simon["red"]["led"].off()
    simon["green"]["button"].when_pressed = simon["green"]["led"].on()
    simon["green"]["button"].when_released = simon["green"]["led"].off()
    simon["yellow"]["button"].when_pressed = simon["yellow"]["led"].on()
    simon["yellow"]["button"].when_released = simon["yellow"]["led"].off()

def start_game_monitor():
    t = threading.Thread(target=start_game)
    t.daemon = True
    t.start()
    t.join()

def main():
    try:
        print("Start new round!!\n")
        init_game()
        start_game_monitor()
    except:
        break
        
if __name__ == "__main__":
    main()
