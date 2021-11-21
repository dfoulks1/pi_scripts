import gpiozero
import threading
import time
import random
import sys
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
        "tone": gpiozero.tones.Tone("C#5")
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
        "tone": gpiozero.tones.Tone("C#4")
        },
    }

def pressed(channel):
    for c in simon.keys():
        if channel is simon[c]["button"]:
            color = simon[c]
        else:
            pass
    
    color["led"].on()
    buzzer.play(color["tone"])

    
def verify_player_selection(channel):
    print("Player Selection:\n")
    global current_step_of_level, current_level, is_won_cur_lvl, is_game_over
    for c in simon.keys():
        if channel is simon[c]["button"]:
            color = simon[c]
            c = c
            break
        else:
            pass
    print(color)
    color["led"].off()
    buzzer.stop()
    print(c)
    if not displaying and not is_won_cur_lvl and not is_game_over:
        if c == pattern[current_step_of_level]:
            current_step_of_level = 1
            if current_step_of_level >= current_level:
                current_level += 1
                is_won_current_level = True
        else:
            is_game_over = True
        buzzer.stop()
        color["led"].off()
        
def add_color_to_pattern():
    global is_won_cur_lvl, current_step_of_level
    is_won_cur_lvl = False
    current_step_of_level - 0
    c = random.randint(0, 3)
    pattern.append(colors[c])

def display_pattern():
    global displaying
    displaying = True
    print("Displaying:\n")
    for i in range(current_level):
        print(pattern[i])
        led = simon[pattern[i]]["led"]
        led.on()
        buzzer.play(simon[pattern[i]]["tone"])
        time.sleep(speed)
        buzzer.stop()
        led.off()
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
            print("Game Over! Your Score was {}\n".format(current_level-1))
            play_again = input("Press 'Y/y' to play again ")
            if play_again.upper() == "Y":
                reset()
                print("Start new round!!\n")
            else:
                print("Thanks for playing\n")
                break
        time.sleep(1)
        
        
def init_game():
    simon["blue"]["button"].when_pressed = pressed
    simon["blue"]["button"].when_released = verify_player_selection
    
    simon["red"]["button"].when_pressed = pressed
    simon["red"]["button"].when_released = verify_player_selection
    
    simon["green"]["button"].when_pressed = pressed
    simon["green"]["button"].when_released = verify_player_selection
    
    simon["yellow"]["button"].when_pressed = pressed
    simon["yellow"]["button"].when_released = verify_player_selection
    
    time.sleep(1)

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
        sys.exit(0)
        
if __name__ == "__main__":
    main()
