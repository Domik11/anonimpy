import time
import math
import colorama
from colorama import Fore, Back, Style, init
import os
colorama.init()




banner_anonim = """
MMMMMMMMMWNNNklllllllllldKNNNWMMMMMMMMMM
MMMMMMMN0occcloooddoooodolcclxXMMMMMMMMM
MMMMMW0ocd000XNNNNNNNNNNNK00OocxXWMMMMMM
MMMMWd;dK0kkkKWWNNNNNNNNNOxxkKOc:0MMMMMM
MMMMWc;KKd:::clo0NNNNXxlcc::lkNd,kMMMMMM
MMMMWc;KNXXNXOc,:kNXOd,,dKNXXXNd,kMMMMMM
MMMMWc,OXKxlclldx0NXKkdoclloOXXl'kMMMMMM
MMMMWc.dOo,...,cdKNXKko;....:kO:'kMMMMMM
MMMMWc,OXKOO00KKO0NXKO0X000O0XXl'kMMMMMM
MMMMWc;0OddxKWNK0KNNX00XWN0xdxKd,kMMMMMM
MMMMWc,k0kk0XNKO0NNNXXO0NNKOkO0l'kMMMMMM
MMMMWc'd0l:xk00d;;ol:;ckKOko:xO:'kMMMMMM
MMMMWl;k0x:..,,..,oc;. .,..'lO0l,OMMMMMM
MMWWWXo:kXOxdkkddOK0OxdxkkdkKKo:ONMMMMMM
MMMMMMKockX000000xcodk00000KKdlkNMMMMMMM
MMMMMMMXl:d0KKXX0; .,dKXKK0kl;kMMMMMMMMM
MMMMMMMMWOlcxKNXO, .,lKNX0ocdKWMMMMMMMMM
MMMMMMMMMMNkolldk: .;dkolldKWMMMMMMMMMMM
MMMMMMMMMMMMWOol:'...,lodKMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNOxxxxxKMMMMMMMMMMMMMMMMM 
"""

bannner_menu = """
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

1.Консоль
2.Сообщения
3.Управление серверами
"""


errorb = """
####### ######  ######  ####### ######  
#       #     # #     # #     # #     # 
#       #     # #     # #     # #     # 
#####   ######  ######  #     # ######  
#       #   #   #   #   #     # #   #   
#       #    #  #    #  #     # #    #  
####### #     # #     # ####### #     #      
"""

load1 = 'Loading .'
load2 = 'Loading ..'
load3 = 'Loading ...'

a = '\nАнонимус: '
c = "console: "
t = "terminal: "
e = '\nElliot: '

def anonimus_loading():
    asdlds = 0
    while asdlds < 2:

        print(Fore.RED)
        print(banner_anonim)
        print(Fore.GREEN)
        print(load1)
        time.sleep(0.5)
        os.system("clear")

        print(Fore.GREEN)
        print(banner_anonim)
        print(Fore.GREEN)
        print(load2)
        time.sleep(0.5)
        os.system("clear")

        print(Fore.RED)
        print(banner_anonim)
        print(Fore.GREEN)
        print(load3)
        time.sleep(0.5)
        os.system("clear")

        asdlds +=  1






def loading(n):

    for i in range(n):
        os.system('clear')
        print('Loading .')
        time.sleep(0.5)
        os.system('clear')
        print('Loading ..')
        time.sleep(0.5)
        os.system('clear')
        print('Loading ...')
        time.sleep(0.5)


def print_text_persona(x,v):
    txt = x
    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
        time.sleep(v)
        print(i, end='', flush=True)
        
def print_text_Elliot():
    xxxx = input('\n'+' Elliot: ')



def print_menu():
    bannner_menu


def dialog_1():

    txt = a + 'ТЫ ХОТЬ В КУРСЕ, ЧТО ТЕБЯ ЛОМАНУЛИ?!\n'
    print_text_persona(txt, 0.03)
    print_text_Elliot()

    txt = a + 'КАКОГО ЧЁРТА ТЫ СПИШЬ?!\n'
    print_text_persona(txt, 0.03)
    print_text_Elliot()

    txt = a + 'Так, сейчас заходи в консоль\n'
    print_text_persona(txt, 0.05)
    print_text_Elliot()

        



    
def scena_udaleniya_virusa():
    vibor = '0'
    while vibor != '1':
        vibor = str(input(t))

        if vibor != '1':
            os.system('clear')
            print(bannner_menu)
    
    txt = '\nВ папке "files" обнаружины вирусы!\n'
    print_text_persona(txt, 0.05)

    txt = '\n(для перехода в папку напишите "cd название папки")\n'
    print_text_persona(txt, 0.05)

    xxx = '0'

    while xxx != 'cd files':
        xxx = str(input(c))

    txt = '\n(для списка файлов напишите "ls")\n'
    print_text_persona(txt, 0.05)


    while xxx != 'ls':
        xxx = str(input(c))

    print("""
        virus.exe
        data
        q123shadhiuq.txt
        1asdfijafiohij.txt
        jksdijasd.fdf
        asdlasdlw.png
        """)


    c_in_files = "\nconsole/files: "

    txt = "\n(Для удаления файла напишите del имя файла.расширение!)\n"
    print_text_persona(txt, 0.05)



    while xxx != 'del virus.exe':
        xxx = str(input(c_in_files))

    os.system('clear')    

    txt = "Файл успешно удалён!"
    print_text_persona(txt, 0.05)

    print("""
        data
        q123shadhiuq.txt
        1asdfijafiohij.txt
        jksdijasd.fdf
        asdlasdlw.png
        """)


    
    txt = "\nУ вас 1 новое сообщение!"
    print_text_persona(txt, 0.05)

    while xxx != 'exit':
        xxx = str(input(c_in_files))

    os.system('clear')
    
    for i in range(3):
        print(Fore.RED)
        print(errorb)
        print(Fore.GREEN)
        print(load1)
        time.sleep(0.5)
        os.system("clear")
            
        print(Fore.GREEN)
        print(errorb)
        print(Fore.GREEN)
        print(load2)
        time.sleep(0.5)
        os.system("clear")



    while xxx != '2':
        os.system('clear')
        print(bannner_menu)
        xxx = str(input(t))


    
def dialog_2():
    txt = '\nАнонимус: Что это было?\n'
    print_text_persona(txt, 0.05)

    txt = 'Анонимус: Чёрт, ты же работаешь на BlueBerryCompany?\n'
    print_text_persona(txt, 0.05)

    txt = 'Анонимус: Это CorpEvil закинули тебе троян!\n'
    print_text_persona(txt, 0.05)

    txt = 'Анонимус: Их хакеры некудышные\n'
    print_text_persona(txt, 0.05)

    txt = 'Анонимус: Они хотели украсть твои данные!\n'
    print_text_persona(txt, 0.05)

    txt = 'Анонимус: Напиши об этом боссу!\n'
    print_text_persona(txt, 0.05)

    xxx = '0'
    while xxx != 'exit':
        xxx = str(input(t))

    print(bannner_menu)

    while xxx != '2':
        xxx = str(input(t))

    os.system('clear')

    print("""  (Telebebra)
    1. Anonimus
    2. Boss
    """)

    xxx = '0'
    while xxx != '2':
        xxx = str(input(t))

    







def dialog_3():
    os.system('clear')
    txt = 'Boss: ЧТО СЛУЧИЛОСЬ?!\n'
    print_text_persona(txt, 0.04)

    txt = e +'Компания CorpEvil меня взломала!\n'
    print_text_persona(txt, 0.05)
            
    txt = '''\nBoss: НУ ТАК СМЕНИ DNS И ЗАПУСТИ
    DDOS НА ИХ СЕРВЕРА!\n'''

    print_text_persona(txt, 0.03)

    txt = 'Boss: Чёртовы хакеры...\n'
    print_text_persona(txt, 0.05)

    txt = 'Boss: Нужно 100.000 ботов\n'
    print_text_persona(txt, 0.05)

    txt = '''Boss: Незабудь скопировать их айпи 101.123.13.121\n'''
    print_text_persona(txt, 0.05)

    xxx = '0'    
    while xxx != 'exit':
        xxx = str(input(t))


def scena_ddos():
    xxx = '0'
    print(bannner_menu)

    while xxx != '1':
        
        xxx = str(input(t))
    os.system('clear')
    print('''Выберите пункт:
    1 - DDos атака
    ''')

    xxx = '0'

    while xxx != '1':
        xxx = str(input(c))

    loading(2)

    print('Введите IP жертвы:\n')

    while xxx != '101.123.13.121':
        xxx = str(input(c))

    print('Введите кол-во ботов:\n')

    while xxx != '100000':
            xxx = str(input(c))

    os.system('clear')


    txt = '''Аттака началась!\n'''
    print_text_persona(txt, 0.05)

    abc = 0

    while abc < 101:
        print('Нагрузка на сервера: ' + str(abc) + '%')
        time.sleep(0.1)
        abc += 1

    print('\n Сервера 101.123.13.121 перегружены!\n')

    print('У вас 1 новое сообщение!\n')

    while xxx != 'exit':
        xxx = str(input(c))

def dialog_4():
    print(bannner_menu)
    xxx = '0'

    while xxx != '2':
        xxx = str(input(t))

    os.system('clear')

    txt = 'Boss: Молодец...\n'
    print_text_persona(txt, 0.05)

    txt = 'Boss: Молодец БЛ*ТЬ!\n'
    print_text_persona(txt, 0.05)

    txt = 'Boss: Я КОМУ ГОВОРИЛ ИЗМЕНИТЬ DNS СЕРВЕР?!\n'
    print_text_persona(txt, 0.02)

    txt = e + '...\n'
    print_text_persona(txt, 0.1)

    txt = 'Boss: всё...\n'
    print_text_persona(txt,0.1) 

    txt = 'Boss: нам п*здeц)\n'
    print_text_persona(txt,0.1)

    txt = e + 'Нужно отклчить наши сервера\n'
    print_text_persona(txt, 0.05)

    txt = 'Boss: Да делай, что хочешь\n'
    print_text_persona(txt,0.1)

    while xxx != 'exit':
        xxx = str(input(t))
    os.system("clear")

def servera_off():
    print(bannner_menu)
    xxx = '0'

    while xxx != '3':
        xxx = str(input(t))
    
    print("""Управление серверами

    1. Выключить серверы
    2. Состояние серверов
    3. DSLADQ%$!!&!
    """)
    xxx = '0'
    xxx = str(input(t))

    if xxx == '1':
        os.system('clear')
        txt = 'Сервера будут выключены на 5 часов\n'
        print_text_persona(txt,0.1)
        time.sleep(2)
        os.system('clear')
        time.sleep(5)
        txt = 'Сервера включены\n'
        print_text_persona(txt,0.1)
        txt = '\nУ вас 1 новое сообщение!\n'
        print_text_persona(txt,0.5)
        while xxx != 'exit':
            xxx = str(input(t))

        print(bannner_menu)

        while xxx != '2':
            xxx = str(input(t))

        txt = 'Анонимус: Ты остановил атаку?\n'
        print_text_persona(txt, 0.05)
        time.sleep(1)
        txt = 'Анонимус: абалдеть\n'
        print_text_persona(txt, 0.05)
        time.sleep(1)
        txt = 'Анонимус: Может сходим сегодня куда-нибудь вечером?)))\n'
        print_text_persona(txt, 0.05)
        time.sleep(2)
        os.system('clear')
        print('Вы прошли игру на хорошую концовку!')
        time.sleep(7)

        




    elif xxx == '2':
        os.system('clear')
        txt = 'Загруженность сервера: 65.9%\n'
        print_text_persona(txt,0.05)
        time.sleep(3)
        servera_off()

    elif xxx == '3':
        os.system('clear')
        print(Fore.RED)
        txt = 'Зачем?\n'
        print_text_persona(txt,0.1)
        time.sleep(2)
        txt = 'Зачем?\n'
        print_text_persona(txt,0.1)
        time.sleep(2)
        txt = 'Теперь мы следим за тобой.\n'
        print_text_persona(txt,0.07)
        time.sleep(2)
        txt = 'Это уже не просто игра на телефоне.\n'
        print_text_persona(txt,0.07)
        time.sleep(2)
        txt = 'Оглянись.\n'
        print_text_persona(txt,0.07)
        time.sleep(2)
        txt = 'Я серьёзно, оглянись.\n'
        print_text_persona(txt,0.07)
        time.sleep(2)
        txt = 'Просто посмотри назад.\n'
        print_text_persona(txt,0.07)

        time.sleep(2)
        os.system('clear')
        abc = 0

        while abc < 101:
            print('Загрузка вредоносного ПО: ' + str(abc) + '%')
            time.sleep(0.05)
            abc += 1

        os.system('clear')

        txt = 'Мы всё слышим.\n'
        print_text_persona(txt,0.07)

        time.sleep(1)

        txt = 'Мы всё видим.\n'
        print_text_persona(txt,0.07)

        time.sleep(2)

        os.system('clear')
        print(Fore.GREEE)


        print('Вы прошли игру на плохую концовку((')

        time.sleep(7)


        

        

        
        














    

    
    





    



    


    

    



    


    


    



    


    
    






