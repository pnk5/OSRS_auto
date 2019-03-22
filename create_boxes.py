from pynput import keyboard
from pynput import mouse
import json

vertical_offset = 40
box_stage = 0
image_num = 1
image = "2019-03-21 (1).png"
listen_click = True
box_num = 0
data = {}

"""Data format should be Data{Image[Box[(x1, y1),(x2, y2)]]}"""

def on_key(key):
    global image_num
    global box_num
    global image
    global listen_click
    global box_stage
    if (key == keyboard.Key.f10):
        print(data)
        with open('imagedata.json', 'w') as fp:
            json.dump(data, fp)
    elif (key == keyboard.Key.f8):
        if listen_click:
            print("Finish box!")
        else:
            box_stage = 0
            listen_click = True
            box_num = 0
            image_num += 1
            image = "2019-03-21 (" + str(image_num) + ")"
            print("New image.")
    elif (key == keyboard.Key.f7):
        listen_click = True
        box_num += 1

key_listener = keyboard.Listener(on_release=on_key)
key_listener.start()

def on_click(x, y, button, pressed):
    if pressed:
        global box_stage
        global data
        global box_num
        global listen_click
        if listen_click:
            if box_stage == 0:
                if box_num == 0:
                    data[image] = [[(x, y + vertical_offset)]]
                else:
                    data[image].append([(x, y + vertical_offset)])
                box_stage += 1
            elif box_stage == 1:
                data[image][box_num].append((x, y + vertical_offset))
                listen_click = False
                print("Box " + str(box_num) + " done.")
                box_stage = 0

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# left corner then bottom corner break loop to next object, key to next image
def box_loop():
    # box_stage = 0
    # box_coords = ()
    while True:
        pass

box_loop()