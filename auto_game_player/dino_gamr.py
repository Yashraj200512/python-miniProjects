import pyautogui as gui
import keyboard
from PIL import Image,ImageGrab
import time
import math

def get_pixel(image,x,y):
    px=image.load()
    return px[x,y]


def get_position():
    while True:
     key=keyboard.read_key()
     if key=='a':
       x,y=gui.position()
       print(f"x:{x} | y:{y}")
              
     if key=='k':
        break
     time.sleep(2)
      
  
def run_game():
  #coordinates are hardcoded
    x,y,w,h=0,350,930,550 #screenshot area
    time.sleep(5)
    xs,x_end=145,245#area between dino and cactus
    while True:
    
      img=gui.screenshot(region=(x,y,w,h))
      img.save("dino.jpg")
      
      for i in reversed(range(xs,x_end)):
        if get_pixel(img,i,150)!=(247,247,247):
          keyboard.press('up')
          print("jumped")
     
    
run_game()


    #only works for cactus rn