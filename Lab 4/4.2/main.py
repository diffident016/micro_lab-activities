try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
from html import HTML
from time import sleep

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'WokwiTalkie AP'
password = '@weArethebest1234'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA_WPA2_PSK)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

ledBlue = Pin(2, Pin.OUT)
ledGreen = Pin(22, Pin.OUT)
ledRed = Pin(23, Pin.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

ledGreen.value(1)
html = HTML()

def get_ledStatus(request):
        
    if request.find('/?led=blink') == 6:
        return 1
    
    if request.find('/?led=alt') == 6:
        return 2
    
    return 0

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  
  request.find('/?led=off')
  
  led_status = get_ledStatus(request)
  
  if led_status == 1:
      ledBlue.value(1)
      ledRed.value(1)
      sleep(0.5)
      ledBlue.value(0)
      ledRed.value(0)
      sleep(0.5)
  
  if led_status == 2:
      ledBlue.value(1)
      sleep(0.5)
      ledBlue.value(0)
      ledRed.value(1)
      sleep(0.5)
      ledRed.value(0)
      
  response = html.web_page(led_status)
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

