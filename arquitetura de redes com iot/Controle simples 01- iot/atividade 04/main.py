import machine                                                                                                                                                 
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(23))
botao = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(14, machine.Pin.OUT)
le =machine.Pin(25, machine.Pin.OUT)
largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True: 
    blue = botao2.value()
    red = botao.value()

    if blue == 0:
        led.value(1), le.value(0)
        tela.fill(0)
        tela.text("umidade da", 0, 0)
        tela.text("sala e:2017", 0, 10)
        tela.show()
        

    if red == 0:
        le.value(1), led.value(0)
        tela.fill(0)
        tela.text("a temperatura", 0, 0)
        tela.text("da sala e: 30", 0, 10)
        tela.text("graus", 0, 20)
        tela.show() 
      
   
