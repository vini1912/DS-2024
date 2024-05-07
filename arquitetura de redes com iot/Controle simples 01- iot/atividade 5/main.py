import machine
from machine import Pin, IC2
import ssd1306

ic2 = IC2(0 , scl=Pin(22), sda=Pin(23))
botao = machine.Pin(4, machine.Pin.IN, machine.Pin.Pull_UP)
botao2 = machine.Pin(16, machine.Pin.IN,machine.Pin.Pull_UP)
botao3 = machine.Pin(18, machine.Pin.IN,machine.Pin.Pull_UP)
botao4 = machine.Pin(19, machine.Pin.IN,machine.Pin.Pull_UP)

largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

tela.text("iluminacao", 10, 0)
tela.text("status", 35, 10)
tela.text("ON/OFF", 31, 20)

while True:

  if botao.value()== 0:
     


