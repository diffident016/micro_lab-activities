try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
from html import HTML

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

html = HTML(ledBlue)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
   
  if led_on == 6:
    ledBlue.value(1)
  if led_off == 6:
    ledBlue.value(0)
  response = html.web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
