# -*- coding: utf-8 -*-

import time
import mouse
import keyboard
import random
import json
with open('setup.json', 'r') as f: 
    data = json.load(f)

# Доступ до значень в JSON файлі і присвоєння їх змінним
but_autoclick = data['buttons']['but_autoclick']
but_autozaj = data['buttons']['but_autozaj']
but_autozona = data['buttons']['but_autozona']
but_off = data['buttons']['but_off']

left_or_right = data['clicks']['left_or_right']
time_autoclick = data['clicks']['time_autoclick']

x1 = data['zone']['x1']
x2 = data['zone']['x2']
y1 = data['zone']['y1']
y2 = data['zone']['y2']

click_1 = data['range_clicks']['click_1']
click_2 = data['range_clicks']['click_2']

time_1 = data['range_delays']['time_1']
time_2 = data['range_delays']['time_2']

work_click = data['work_status']['work_click']
work_zaj = data['work_status']['work_zaj']
work_zona = data['work_status']['work_zona']


left_or_right = "left"
time_autoclick = 1 # время между кликами (автокликер)
   
def auto_zona():
   global work_zona
   work_zona = True

def auto_click():
   global work_click
   work_click = True
    

def auto_zaj():
   global work_zaj
   work_zaj = True
    
def off():
   global work_zaj, work_click, work_zona
   work_click = False
   work_zona = False
   if work_zaj == True:
       mouse.release(button=left_or_right)
       work_zaj = False
    
    
keyboard.add_hotkey(but_autoclick, auto_click)
keyboard.add_hotkey(but_autozaj, auto_zaj)
keyboard.add_hotkey(but_autozona, auto_zona)
keyboard.add_hotkey(but_off, off) 
while True:
   while work_click:
       mouse.click(left_or_right)
       time.sleep(time_autoclick)
       
   while work_zona:
      x_coord = random.randint(x1, x2)
      y_coord = random.randint(y1, y2)
      random_click = random.randint(click_1, click_2)
      random_time = random.uniform(time_1, time_2)
      for i in range(random_click):
         mouse.move(x_coord, y_coord)
         mouse.click(left_or_right)
         time.sleep(random_time)

   
   if work_zaj == True:
       mouse.press(button=left_or_right) 
       time.sleep(5)
