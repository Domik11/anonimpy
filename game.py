import time
import math
import colorama
from colorama import Fore, Back, Style, init
import os
import h

colorama.init()

#game v1.2
c = "console: "
t = "terminal: "


os.system("clear")

h.anonimus_loading()
h.print_text_persona('У вас 1 новое сообщение!\n', 0.1)
print('1 - Открыть')

vibor = '0'

while vibor != '1':
    vibor = input(t)

    if vibor != '1':
        os.system("clear")
        h.print_text_persona('У вас новое сообщение!', 0.1)
        print('1 - Открыть\n')
os.system("clear")


h.dialog_1()


viborxdxd = '101010101010'
while viborxdxd != 'exit':
    os.system('clear')
    print('\n'+'Чтобы выйти введите "exit": ')
    viborxdxd = str(input(t))
        




#сцена удаления вируса
h.scena_udaleniya_virusa()

#диалог 2
h.dialog_2()
#диалог 3
h.dialog_3()

#DDOS
h.scena_ddos()


h.dialog_4()
h.servera_off()


