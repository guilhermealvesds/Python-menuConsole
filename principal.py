import os
from pynput import keyboard

vMenu = 1

class bcolors:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'
    BLUE_WHITE_INICIO = '\033[0;37;44m'
    BLUE_WHITE_FIM = '\033[0m 0;37;44m'
    BLACK_WHITE_INICIO = '\033[0;37;48m'
    BLACK_WHITE_FIM = '\033[0m 0;37;48m'

def on_press(key):
	pass

def on_release(key):
	global vMenu
	if key == keyboard.Key.esc:
		return False
	if key == keyboard.Key.down:
		if vMenu >= 1 and vMenu < 3:
			vMenu += 1
	if key == keyboard.Key.up:
		if vMenu <= 3 and vMenu > 1:
			vMenu -= 1
	if key == keyboard.Key.left:
		if vMenu == 4:
			vMenu = 1
	if key == keyboard.Key.right:
		if vMenu == 1:
			vMenu = 4
	criaMenu()
		
def limparTela():
	os.system('clear') or None

def criaMenu():
	global vMenu
	limparTela()
	print(bcolors.OKBLUE + "╔══════════════════════════════════════════════════════════╗" + bcolors.ENDC)
	
	if vMenu == 1:
		print(bcolors.OKBLUE + "║" + bcolors.BLUE_WHITE_INICIO  + " HOSPEDAGEM " + bcolors.ENDC + bcolors.OKBLUE  + " " + bcolors.BLACK_WHITE_INICIO  + " SERVIÇOS " + bcolors.ENDC + bcolors.OKBLUE + "                                   ║ " + bcolors.ENDC)
	else:
		if vMenu == 4:
			print(bcolors.OKBLUE + "║" + bcolors.BLACK_WHITE_INICIO + " HOSPEDAGEM " + bcolors.ENDC + bcolors.OKBLUE + " " + bcolors.BLUE_WHITE_INICIO  + " SERVIÇOS " + bcolors.ENDC + bcolors.OKBLUE + "                                   ║ " + bcolors.ENDC)
		else:
			print(bcolors.OKBLUE + "║" + bcolors.BLACK_WHITE_INICIO + " HOSPEDAGEM " + bcolors.ENDC + bcolors.OKBLUE + " " + bcolors.BLACK_WHITE_INICIO  + " SERVIÇOS " + bcolors.ENDC + bcolors.OKBLUE + "                                   ║ " + bcolors.ENDC)
	
	if vMenu == 2:
		print(bcolors.OKBLUE + "║" + bcolors.BLUE_WHITE_INICIO + " QUARTOS    " + bcolors.ENDC + bcolors.OKBLUE + "                                              ║ " + bcolors.ENDC)
	else:
		print(bcolors.OKBLUE + "║" + bcolors.BLACK_WHITE_INICIO + " QUARTOS    " + bcolors.ENDC + bcolors.OKBLUE + "                                              ║ " + bcolors.ENDC)
	
	if vMenu == 3:
		print(bcolors.OKBLUE + "║" + bcolors.BLUE_WHITE_INICIO + " RESERVAS   " + bcolors.ENDC + bcolors.OKBLUE + "                                              ║ " + bcolors.ENDC)
	else:
		print(bcolors.OKBLUE + "║" + bcolors.BLACK_WHITE_INICIO + " RESERVAS   " + bcolors.ENDC + bcolors.OKBLUE + "                                              ║ " + bcolors.ENDC)
			
	print(bcolors.OKBLUE + "║                                                          ║" + bcolors.ENDC)
	print(bcolors.OKBLUE + "║                                                          ║" + bcolors.ENDC)
	print(bcolors.OKBLUE + "║                                                          ║" + bcolors.ENDC)
	print(bcolors.OKBLUE + "╚══════════════════════════════════════════════════════════╝" + bcolors.ENDC)

criaMenu()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
